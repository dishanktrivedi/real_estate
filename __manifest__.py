{
    # Name of the module, will be shown in the Apps menu
    'name': 'Real Estate',
    'version': '1.0',
    'author': 'Dishank Trivedi',
    'category': 'Uncategorized',
    'summary': 'Real Estate Application',
    'depends': ['base'],

    # List of XML files for views
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/inherited_model_views.xml',
        'views/estate_menus.xml',
    ],


    # Allows the module to be installed
    'installable': True,

    # Marks the module as a standalone application
    'application': True,
}