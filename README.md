# real_estate
Odoo Real Estate Application 

**Exercise**
Define the real estate properties model.
Based on example given in the CRM module, create the appropriate files and folder for the estate_property table.
When the files are created, add a minimum definition for the estate.property model.

**Exercise**
Add a description.
Add a _description to your model to get rid of one of the warnings.

**Exercise**
Add basic fields to the Real Estate Property table.
Add the following basic fields to the table:

Field Type              name

Char                    description

Text                    postcode

Char                    date_availability

Date                    expected_price

Float                   selling_price

Float                   bedrooms

Integer                 living_area

Integer                 facades

Integer                 garage

Boolean                 garden

Boolean                 garden_area

Integer                 garden_orientation

Selection               The garden_orientation field must have 4 possible values: “North”, “South”, “East” and “West”. 
                        The selection list is defined as a list of tuples.



**Exercise**
Set attributes for existing fields.
Add the following attributes:

Field                       Attribute

name                        required

expected_price              required
After restarting the server, both fields should be not nullable.