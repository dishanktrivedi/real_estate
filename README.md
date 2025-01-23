# Real Estate

Welcome to the **Odoo Real Estate Application**! This module helps manage real estate properties, property types, offers, and more within the Odoo ERP system.

---

## 📋 **Exercise Overview**

### 1️⃣ Define the Real Estate Properties Model

- Create files and folders for the `estate_property` table.
- Add a minimum definition for the `estate.property` model.

### 2️⃣ Add Descriptions

- Implement `_description` to avoid warnings.

### 3️⃣ Add Basic Fields to the Property Table

| Field Name          | Type                   |
| ------------------- | ---------------------- |
| name                | Char                   |
| description         | Text                   |
| postcode            | Char                   |
| date\_availability  | Date                   |
| expected\_price     | Float                  |
| selling\_price      | Float                  |
| bedrooms            | Integer                |
| living\_area        | Integer                |
| facades             | Integer                |
| garage              | Boolean                |
| garden              | Boolean                |
| garden\_area        | Integer                |
| garden\_orientation | Selection (N, S, E, W) |

### 4️⃣ Set Field Attributes

- Make `name` and `expected_price` fields **required**.

### 5️⃣ Define Access Rights

- Create `ir.model.access.csv` and define in `__manifest__.py`.

### 6️⃣ Add Actions and Menus

- Create `estate_property_views.xml` and `estate_menus.xml`.
- Implement property action and hierarchical menus.

### 7️⃣ Configure Default Values

- Set default bedrooms to `2` and availability date to `3 months`.

### 8️⃣ Implement State Field

- Define states: **New, Offer Received, Offer Accepted, Sold, Canceled**.

### 9️⃣ Custom Views

- Create **list, form, and search views** with filters and groupings.

### 🔟 Add Related Models

- **Property Type:** Define model and add to form views.
- **Property Tag:** Create tags with color options.
- **Property Offer:** Define price, status, and relations.

### 1️⃣1️⃣ Business Logic

- Compute total area and best offer.
- Implement constraints for prices.

### 1️⃣2️⃣ Interactive Features

- Add buttons for "Accept", "Refuse", "Sold", "Cancel".
- Set domain filters and stat buttons.

### 1️⃣3️⃣ UI Enhancements

- Add decorations to property lists.
- Use **status bar** and widget options.

### 1️⃣4️⃣ Security & Permissions

- Implement access controls and conditional visibility.

---


## ⚡ **Features**

- Property listing management
- Offer tracking and validation
- Advanced search and filters

---

## 🛠 **Technologies Used**

- **Odoo 17**
- **Python**
- **XML**
- **PostgreSQL**

---


## 📧 **Contact**

For any questions, feel free to reach out:

- **Email:** [dishanktrivedi98@gmail.com](mailto\:dishanktrivedi98@gmail.com)
---

> **Note:** This is an educational project based on Odoo's official documentation and best practices.

---
