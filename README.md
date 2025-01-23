# real_estate
Odoo Real Estate Application 

**Exercise**
Define the real estate properties model.
Based on example given in the CRM module, create the appropriate files and folder for the estate_property table.
When the files are created, add a minimum definition for the estate.property model.
<br><br>

**Exercise**
Add a description.
Add a _description to your model to get rid of one of the warnings.
<br><br>
**Exercise**
Add basic fields to the Real Estate Property table.
Add the following basic fields to the table:
Field Type_________name
Char_______________description
Text_______________postcode
Char_______________date_availability
Date_______________expected_price
Float______________selling_price
Float______________bedrooms
Integer____________living_area
Integer____________facades
Integer____________garage
Boolean____________garden
Boolean____________garden_area
Integer____________garden_orientation
Selection__________The garden_orientation field must have 4 possible values: “North”, “South”, “East” and “West”. 
<br><br>


**Exercise**
Set attributes for existing fields.
Add the following attributes:
Field_______________Attribute
name________________required
expected_price______required
After restarting the server, both fields should be not nullable.
<br><br>


**Exercise**
Add access rights.
Create the ir.model.access.csv file in the appropriate folder and define it in the __manifest__.py file.
Give the read, write, create and unlink permissions to the group base.group_user.
<br><br>

**Exercise**
Add an action.
Create the estate_property_views.xml file in the appropriate folder and define it in the __manifest__.py file.
Create an action for the model estate.property.
<br><br>

**Exercise**
Add menus.
Create the estate_menus.xml file in the appropriate folder and define it in the __manifest__.py file. Remember the sequential loading of the data files ;-)
Create the three levels of menus for the estate.property action created in the previous exercise. Refer to the Goal of this section for the expected result.
<br><br>

**Exercise**
Add new attributes to the fields.
Find the appropriate attributes (see Field) to:
set the selling price as read-only
prevent copying of the availability date and the selling price values
<br><br>

**Exercise**
Set default values.
Add the appropriate default attributes so that:
the default number of bedrooms is 2
the default availability date is in 3 months
<br><br>

**Exercise**
Add active field.
Add the active field to the estate.property model.
<br><br>

**Exercise**
Set a default value for active field.
Set the appropriate default value for the active field so it doesn’t disappear anymore.
<br><br>

**Exercise**
Add state field.
Add a state field to the estate.property model. Five values are possible: New, Offer Received, Offer Accepted, Sold and Canceled. It must be required, should not be copied and should have its default value set to “New”.
Make sure to use the correct type!
<br><br>

**Exercise**
Add a custom list view.
Define a list view for the estate.property model in the appropriate XML file. Check the Goal of this section for the fields to display.
<br><br>

**Exercise**
Add a custom form view.
Define a form view for the estate.property model in the appropriate XML file. Check the Goal of this section for the expected final design of the page.
<br><br>

**Exercise**
Add a custom search view.
Define a search view for the estate.property model in the appropriate XML file. Check the first image of this section’s Goal for the list of fields.
<br><br>

**Exercise**
Add filter and Group By.
The following should be added to the previously created search view:
a filter which displays available properties, i.e. the state should be “New” or “Offer Received”.
the ability to group results by postcode.
<br><br>

**Exercise**
Add the Real Estate Property Type table.
Create the estate.property.type model and add the following field:
Field__________Type__________Attributes
name___________Char__________required
Add the field property_type_id into your estate.property model and its form, tree and search views
<br><br>

**Exercise**
Add the buyer and the salesperson.
Add a buyer and a salesperson to the estate.property model using the two common models mentioned above. They should be added in a new tab of the form view.
The default value for the salesperson must be the current user. The buyer should not be copied.
<br><br>

**Exercise**
Add the Real Estate Property Tag table.
Create the estate.property.tag model and add the following field:
Field_________Type__________Attributes
name__________Char__________required
Add the field tag_ids to your estate.property model and in its form and tree views.
<br><br>

**Exercise**
Add the Real Estate Property Offer table.
Create the estate.property.offer model and add the following fields:
Field_______________Type____________________________Attributes__________Values
price_______________Float
status______________Selection_______________________no copy__________Accepted, Refused
partner_id__________Many2one (res.partner)__________required
property_id_________Many2one (estate.property)______required
Create a tree view and a form view with the price, partner_id and status fields. No need to create an action or a menu.
Add the field offer_ids to your estate.property model and in its form view.
<br><br>

**Exercise**
Compute the total area.
Add the total_area field to estate.property. It is defined as the sum of the living_area and the garden_area.
Add the field in the form view.
<br><br>

**Exercise**
Compute the best offer.
Add the best_price field to estate.property. It is defined as the highest (i.e. maximum) of the offers” price.
Add the field to the form view.
<br><br>

**Exercise**
Compute a validity date for offers.
Add the following fields to the estate.property.offer model:
Field_____________Type__________Default
validity__________Integer__________7
date_deadline_____Date
Where date_deadline is a computed field which is defined as the sum of two fields from the offer: the create_date and the validity. Define an appropriate inverse function so that the user can set either the date or the validity.
<br><br>

**Exercise**
Set values for garden area and orientation.
Create an onchange in the estate.property model in order to set values for the garden area (10) and orientation (North) when garden is set to True. When unset, clear the fields.
<br><br>

**Exercise**
Cancel and set a property as sold.
Add the buttons “Cancel” and “Sold” to the estate.property model. A canceled property cannot be set as sold, and a sold property cannot be canceled.
Add the buttons “Accept” and “Refuse” to the estate.property.offer model.
When an offer is accepted, set the buyer and the selling price for the corresponding property.
Pay attention: in real life only one offer can be accepted for a given property!
<br><br>

**Exercise**
Add SQL constraints.
Add the following constraints to their corresponding models:
A property expected price must be strictly positive
A property selling price must be positive
An offer price must be strictly positive
A property tag name and property type name must be unique
<br><br>

**Exercise**
Add Python constraints.
Add a constraint so that the selling price cannot be lower than 90% of the expected price.
<br><br>

**Exercise**
Add an inline list view.
Add the One2many field property_ids to the estate.property.type model.
Add the field in the estate.property.type form view.
<br><br>

**Exercise**
Use the status bar widget.
Use the statusbar widget in order to display the state of the estate.property.
<br><br>

**Exercise**
Add model ordering.
Define the following orders in their corresponding models:
Model_________________________Order
estate.property_______________Descending ID
estate.property.offer_________Descending Price
estate.property.tag___________Name
estate.property.type__________Name
<br><br>

**Exercise**
Add manual ordering.
Add the following field:
Model______________________Field_____________Type
estate.property.type_______Sequence__________Integer
Add the sequence to the estate.property.type list view with the correct widget.
<br><br>

**Exercise**
Add widget options.
Add the appropriate option to the property_type_id field to prevent the creation and the editing of a property type from the property form view. Have a look at the Many2one widget documentation for more info.
Add the following field:
Model_________________Field_________________Type
estate.property.tag___Color_________________Integer
Then add the appropriate option to the tag_ids field to add a color picker on the tags.
<br><br>

**Exercise**
Add conditional display of buttons.
Use the invisible attribute to display the header buttons conditionally as depicted in this section’s Goal (notice how the “Sold” and “Cancel” buttons change when the state is modified).
<br><br>


**Exercise**
Use invisible.
Make the garden area and orientation invisible in the estate.property form view when there is no garden.
Make the “Accept” and “Refuse” buttons invisible once the offer state is set.
Do not allow adding an offer when the property state is “Offer Accepted”, “Sold” or “Canceled”. To do this use the readonly attribute.
<br><br>

**Exercise**
Make list views editable.
Make the estate.property.offer and estate.property.tag list views editable.
<br><br>

**Exercise**
Make a field optional.
Make the field date_availability on the estate.property list view optional and hidden by default.
<br><br>

**Exercise**
Add some decorations.
On the estate.property list view:
  Properties with an offer received are green
  Properties with an offer accepted are green and bold
  Properties sold are muted
On the estate.property.offer list view:
  Refused offers are red
  Accepted offers are green
  The state should not be visible anymore

<br><br>

**Exercise**
Add a default filter.
Make the “Available” filter selected by default in the estate.property action.
<br><br>

**Exercise**
Change the living area search.
Add a filter_domain to the living area to include properties with an area equal to or greater than the given value.
<br><br>

**Exercise**
Add a stat button to property type.
  Add the field property_type_id to estate.property.offer. We can define it as a related field on property_id.property_type_id and set it as stored.
Thanks to this field, an offer will be linked to a property type when it’s created. You can add the field to the list view of offers to make sure it works.
  Add the field offer_ids to estate.property.type which is the One2many inverse of the field defined in the previous step.
  Add the field offer_count to estate.property.type. It is a computed field that counts the number of offers for a given property type (use offer_ids to do so).
At this point, you have all the information necessary to know how many offers are linked to a property type. When in doubt, add offer_ids and offer_count directly to the view. The next step is to display the list when clicking on the stat button.
  Create a stat button on estate.property.type pointing to the estate.property.offer action. This means you should use the type="action" attribute.
At this point, clicking on the stat button should display all offers. We still need to filter out the offers.
  On the estate.property.offer action, add a domain that defines property_type_id as equal to the active_id.
<br><br>

**Exercise**
Add business logic to the CRUD methods.
  Prevent deletion of a property if its state is not “New” or “Canceled”
  At offer creation, set the property state to “Offer Received”. Also raise an error if the user tries to create an offer with a lower amount than an existing offer.
<br><br>

**Exercise**
Add a field to Users.
Add the following field to res.users:
Field_________________Type
property_ids__________One2many inverse of the field that references the salesperson in estate.property
Add a domain to the field so it only lists the available properties.
<br><br>

**Exercise**
Add fields to the Users view.
Add the property_ids field to the base.view_users_form in a new notebook page.
<br><br>

**Exercise**
Create a link module.
Create the estate_account module, which depends on the estate and account modules.
<br><br>

**Exercise**
Add the first step of invoice creation.
Create a estate_property.py file in the correct folder of the estate_account module.
_inherit the estate.property model.
Override the action_sold method (you might have named it differently) to return the super call.
<br><br>

**Exercise**
Add the second step of invoice creation.
Create an empty account.move in the override of the action_sold method:
the partner_id is taken from the current estate.property
the move_type should correspond to a “Customer Invoice”
<br><br>

**Exercise**
Add the third step of invoice creation.
Add two invoice lines during the creation of the account.move. Each property sold will be invoiced following these conditions:
6% of the selling price
an additional 100.00 from administrative fees.
<br><br>

**Exercise**
Make a minimal kanban view.
Using the simple example provided, create a minimal Kanban view for the properties. The only field to display is the name.
<br><br>

**Exercise**
Improve the Kanban view.
Add the following fields to the Kanban view: expected price, best price, selling price and tags. Pay attention: the best price is only displayed when an offer is received, while the selling price is only displayed when an offer is accepted.
<br><br>

**Exercise**
Add default grouping.
Use the appropriate attribute to group the properties by type by default. You must also prevent drag and drop.
<br><br>
