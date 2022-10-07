import petl as etl
import datetime
from crm.models.account import Account
from crm.models.contact import Contact
from crm.models.level import Level
from crm.models.location import Location
from crm.models.opportunity import Opportunity
from crm.models.opportunitycontact import OpportunityContact
from crm.models.role import Role
from crm.models.skill import Skill

file = etl.fromcsv("jupyter/global_demand.csv")


def contact_sync(contact: Contact) -> Contact:
    existing_contact = None
    contacts = Contact.objects

    if contact.email:
        existing_contact = contacts.filter(email=contact.email).first()
    elif contact.first_name and contact.last_name:
        existing_contact = contacts.filter(
            first_name=contact.first_name, last_name=contact.last_name
        ).first()
    elif contact.first_name:
        existing_contact = contacts.filter(
            first_name=contact.first_name, last_name__isnull=True, email__isnull=True
        ).first()

    if existing_contact:
        return existing_contact
    else:
        contact.save()
        return contact


def contact_builder(name: str, **kwargs) -> {Contact, None}:
    domain = kwargs.get("domain", "accenture.com")
    # role = kwargs.get('role', Contact.ROLE_PRIMARY)

    if not name:
        return None

    if "," in name:
        last_name, first_name = name.split(", ")
        email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
        display_name = name
    elif "." in name:
        # first_name, last_name = name.split(".")
        # email = f"{ name }@{ domain }"
        first_name, *last_names = name.split(".")
        last_name = " ".join(last_names)
        alias = ".".join(map(lambda r: r.lower(), [first_name] + last_names))
        email = f"{alias}@{domain}"
        display_name = " ".join(map(lambda w: w.capitalize(), name.split(".")))
    elif " " in name:
        first_name, *last_names = name.split(" ")
        last_name = " ".join(last_names)
        alias = ".".join(map(lambda r: r.lower(), [first_name] + last_names))
        email = f"{alias}@{domain}"
        display_name = name
    else:
        first_name = name
        last_name = None
        email = None
        display_name = name

    return contact_sync(
        Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            display_name=display_name,
            # role=role,
        )
    )


def location_builder(row: any) -> Location:
    location, created = Location.objects.get_or_create(
        location=row.location, country=row.country, region=row.region
    )
    return location


def account_builder(row: any) -> Account:
    account, account_created = Account.objects.get_or_create(
        account_name=row.account_name
    )
    return account


def opportunity_builder(row: any) -> Opportunity:
    # role = kwargs.get('role', Contact.ROLE_PRIMARY)
    opportunity, created = Opportunity.objects.get_or_create(
        opportunity_name=row.opportunity_name
    )
    return opportunity


def opportunity_contact_builder(**kwargs) -> OpportunityContact:
    role = kwargs.get("role")
    contact_role = kwargs.get("contact_role", OpportunityContact.ROLE_PRIMARY)
    opportunity = kwargs.get("opportunity")
    contact = kwargs.get("contact")

    assert role
    assert contact_role
    assert opportunity
    assert contact

    contact, created = OpportunityContact.objects.get_or_create(
        role=role, contact_role=contact_role, opportunity=opportunity, contact=contact
    )

    return contact


def skill_builder(row: any) -> Skill:
    skillset, created = Skill.objects.get_or_create(name=row.primary_skill)
    return skillset


def level_builder(title: str, number: str) -> Level:
    level, created = Level.objects.get_or_create(title=title, number=number)
    return level


def role_builder(row: any) -> {Role, None}:
    if not row.role_name or not row.import_key:
        return

    primary_contact = contact_builder(row.primary_contact)
    key_contact = contact_builder(row.key_contact)
    location = location_builder(row)
    account = account_builder(row)
    opportunity = opportunity_builder(row)
    primary_skill = skill_builder(row)

    role = Role.objects.filter(import_key=row.import_key)
    if not role:
        role = Role.objects.create(
            opportunity=opportunity,
            name=row.role_name,
            requirements=row.requirements,
            location=location,
            state=row.state,
            primary_skill=primary_skill,
            secondary_skills=row.secondary_skills,
            valid_from=row.valid_from,
            valid_till=row.valid_till,
            from_level=level_builder(row.from_level_group, row.from_level_detail),
            to_level=level_builder(row.to_level_group, row.to_level_detail),
            import_key=row.import_key,
        )
        account.opportunities.add(opportunity)
    else:
        role.update(state=row.state)
        role = role.first()

    if primary_contact:
        opportunity_contact_builder(
            contact=primary_contact,
            role=role,
            contact_role=OpportunityContact.ROLE_PRIMARY,
            opportunity=opportunity,
        )

    if key_contact:
        opportunity_contact_builder(
            contact=key_contact,
            role=role,
            contact_role=OpportunityContact.ROLE_KEYCONTACT,
            opportunity=opportunity,
        )

    return row.import_key


def etl_task(file: str) -> None:
    global_demand_cleaned = (
        etl.fromcsv(file)
        .cut(
            "Project Client",
            "Role Fulfillment Contact",
            "Role Primary Contact",
            "Project",
            "Role Title",
            "Role Description",
            "Role Status",
            "Role Start Date",
            "Role End Date",
            "Role Work Location",
            "Role Country/Territory",
            "Role Market Unit Location",
            "Role Primary Skill Category",
            "Role Skills",
            "Role Management Level Group From",
            "Role Management Level From",
            "Role Management Level Group To",
            "Role Management Level To",
            "Role #",
        )
        .rename(
            {
                "Role Title": "role_name",
                "Role Description": "requirements",
                "Role Status": "state",
                "Role Start Date": "valid_from",
                "Role End Date": "valid_till",
                "Role Work Location": "location",
                "Role Country/Territory": "country",
                "Role Market Unit Location": "region",
                "Role Skills": "secondary_skills",
                "Role Primary Skill Category": "primary_skill",
                "Role Management Level Group From": "from_level_group",
                "Role Management Level From": "from_level_detail",
                "Role Management Level Group To": "to_level_group",
                "Role Management Level To": "to_level_detail",
                "Role #": "import_key",
                "Project Client": "account_name",
                "Role Fulfillment Contact": "key_contact",
                "Role Primary Contact": "primary_contact",
                "Project": "opportunity_name",
            }
        )
        .convert(
            {
                "valid_from": lambda v: datetime.datetime.strptime(v, "%m/%d/%Y"),
                "valid_till": lambda v: datetime.datetime.strptime(v, "%m/%d/%Y"),
            }
        )
        .addfield("role", role_builder)
    )

    for r in global_demand_cleaned:
        pass