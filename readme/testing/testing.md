## **CONTENTS**

- [User Stories](#user-stories)
- [Security](#security)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Code Validation](#code-validation)
- [Accesibility Validation](#accesibility-validation)
- [Responsive and Browsers](#responsive-and-browsers)

---

## **User Stories**

- As a customer, I would like to easily navigate through the website.
  - The main navigation has 5 sections available across all pages.
  ![images](/readme/media/user-stories/nav-bar.png)
  - At different parts of the site some button links will redirect you to the checkout page or back to the product page.
  ![images](/readme/media/user-stories/button-links.png)
- As a customer, I would like to easily identify what products are available.
  - On the homepage, there is a button there that is linked to the product page.
  ![images](/readme/media/user-stories/homepage-button.png)
  - There is a link to the product page at the top of the navigation bar, which if clicked a drop-down menu will be available.
  ![images](/readme/media/user-stories/shop-nav.png)
  - The products are easily readable and there is a name description and price underneath the image.
  ![images](/readme/media/user-stories/products.png)
- As a customer, I would like to see a description of the product.
  - When the customer clicks the product they would like to see, they get a description of the products and also the measurements of the sizes.
  ![images](/readme/media/user-stories/product-info.png)
- As a customer, I would like to search for a specific product by a keyword.
  - Above the navigation menu there is a search bar which the customer can search for a product or a keyword.
  ![images](/readme/media/user-stories/search-product.png)
- As a customer, I would like to add products to my shopping bag.
  - When the customer clicks the product, they can select that product from the bottom of the page to add this to their bag.
  ![images](/readme/media/user-stories/add-product.png)
- As a customer, I would like to be notified when adding an item to my shopping bag.
  - When the product has been added to the bag, the customer will get a notification that this has been added.
  ![images](/readme/media/user-stories/shopping-bag.png)
- As a customer, I would like to edit or delete an item from my shopping bag.
  - From the bag section, the customer can update or delete the items they have selected.
  ![images](/readme/media/user-stories/edit-delete.png)
  - When the item has been deleted or updated, the user will receive a alert to remind them what item has been removed.
  ![images](/readme/media/user-stories/delete-message.png)
- As a customer, I would like to see my previous orders.
  - On the user profile page there is a list of the user's previous orders.
  ![images](/readme/media/user-stories/order-history.png)
  - When the user clicks on an order number they will be brought to the details of that order and also get an alert.
  ![images](/readme/media/user-stories/order-history-info.png)
  ![images](/readme/media/user-stories/order-alert.png)

  [Back to contents](#contents)

---

## **Security**

- Environmental Variables
  - For security reasons, I used os to declare my environmental variables for any sensitive information.
  - All sensitive information was placed in an env.py file for the Development.
  - To deploy to Heroku, these were placed in the settings, config variables section.
- User's Passwords
  - I used Django all auth to handle the user's login details and signup.
  - This stores the user's passwords as a hash key for security.

[Back to contents](#contents)

---

## **Manual Testing**

### **Feature testing**
 - All functionality of the website was also tested manually to ensure it all worked correctly.
   - Shopping Bag
     - ?????
   - Payment
     - ????
   - Adding Products
     - ????
   - Deleting Products
     - ????
   - Editing Products
     - ????
   - Profile
     - ????
   - Size Selection
     - ????

[Back to contents](#contents)

---

## **Bugs**

Bug | Fix
--------|--------
Products_product does not exist | There were no connections in my PostgreSQL on Heroku, so I loaded my categories and products in Github again, which solved the issue.
Receiving a 500 error and my CSS was not loading | I had to change the debug to 'DEVELOPMENT' in os.environ and export the debug to be True to get the CSS to load.
Aws no activated |I had some trouble activating my AWS account to access the s3/bucket section but the support team at AWS helped me sort this out.

[Back to contents](#contents)

---

## **Code Validation**
- Html
  - Add Products Page - [view](/readme/media/test/html/add-product.png)
  - Edit Products Page - [view](/readme/media/test/html/edit-product.png)
  - Checkout Success Page - [view](/readme/media/test/html/checkout-success.png)
  - Checkout Page - [view](/readme/media/test/html/checkout.png)
  - Bag Page - [view](/readme/media/test/html/bag.png)
  - Order History Page - [view](/readme/media/test/html/order-history.png)
  - Login Page - [view](/readme/media/test/html/login.png)
  - All Products Page - [view](/readme/media/test/html/all-products.png)
  - Single Products Page - [view](/readme/media/test/html/products-single.png)
  - Profile Page - [view](/readme/media/test/html/profile.png)
  - Sign Up Page - [view](/readme/media/test/html/sign-up.png)
  - Home Page - [view](/readme/media/test/html/homepage.png)
  - Add Blog Page - [view](/readme/media/test/html/add-blog.png)
  - Single Blog Page - [view](/readme/media/test/html/single-blog.png)
  - All Blog Page - [view](/readme/media/test/html/all-blog.png)

- Css
  - Add Products Page - [view](/readme/media/test/css/add-product.png)
  - Edit Products Page - [view](/readme/media/test/css/edit-product.png)
  - Checkout Success Page - [view](/readme/media/test/css/checkout-success.png)
  - Checkout Page - [view](/readme/media/test/css/checkout.png)
  - Bag Page - [view](/readme/media/test/css/bag.png)
  - Order History Page - [view](/readme/media/test/css/order-history.png)
  - Login Page - [view](/readme/media/test/css/login.png)
  - All Products Page - [view](/readme/media/test/css/all-products.png)
  - Single Products Page - [view](/readme/media/test/css/single-categories.png)
  - Profile Page - [view](/readme/media/test/css/profile.png)
  - Sign Up Page - [view](/readme/media/test/css/sign-up.png)
  - Home Page - [view](/readme/media/test/css/home.png)
  - Add Blog Page - [view](/readme/media/test/css/add-blog.png)
  - Single Blog Page - [view](/readme/media/test/css/single-blog.png)
  - All Blog Page - [view](/readme/media/test/css/all-blog.png)

- Js
  - Checkout - [view](/readme/media/test/js/checkout.png)
  - Profile - [view](/readme/media/test/js/profile.png)
  - Stripe Element - [view](/readme/media/test/js/stripe-element.png)

- Python
  - Manage.py - [view](/readme/media/test/python/manage.png)
  - Custom Storage.py - [view](/readme/media/test/python/custom-storage.png)

  - Bag
    - Apps.py - [view](/readme/media/test/python/bag/apps.png)
    - Context.py - [view](/readme/media/test/python/bag/context.png)
    - Urls.py - [view](/readme/media/test/python/bag/urls.png)
    - Views.py - [view](/readme/media/test/python/bag/views.png)
  - Checkout
    - Apps.py - [view](/readme/media/test/python/checkout/apps.png)
    - Admin.py - [view](/readme/media/test/python/checkout/admin.png)
    - Urls.py - [view](/readme/media/test/python/checkout/urls.png)
    - Views.py - [view](/readme/media/test/python/checkout/views.png)
    - Forms.py - [view](/readme/media/test/python/checkout/forms.png)
    - Models.py - [view](/readme/media/test/python/checkout/models.png)
    - Signals.py - [view](/readme/media/test/python/checkout/signals.png)
    - Webhook Handler.py - [view](/readme/media/test/python/checkout/webhook-handlers.png)
    - Webhook.py - [view](/readme/media/test/python/checkout/webhooks.png)
  - Hanks
    - Asgi.py - [view](/readme/media/test/python/hanks/asgi.png)
    - Settings.py - [view](/readme/media/test/python/hanks/settings.png)
    - Urls.py - [view](/readme/media/test/python/hanks/urls.png)
    - Wsgi.py - [view](/readme/media/test/python/hanks/wsgi.png)
  - Products
    - Admin.py - [view](/readme/media/test/python/products/admin.png)
    - Apps.py - [view](/readme/media/test/python/products/apps.png)
    - Forms.py - [view](/readme/media/test/python/products/forms.png)
    - Models.py - [view](/readme/media/test/python/products/models.png)
    - Urls.py - [view](/readme/media/test/python/products/urls.png)
    - Views.py - [view](/readme/media/test/python/products/views.png)
    - Widgets.py - [view](/readme/media/test/python/products/widgets.png)
  - Profile
    - Apps.py - [view](/readme/media/test/python/profile/apps.png)
    - Forms.py - [view](/readme/media/test/python/profile/forms.png)
    - Models.py - [view](/readme/media/test/python/profile/models.png)
    - Urls.py - [view](/readme/media/test/python/profile/urls.png)
    - Views.py - [view](/readme/media/test/python/profile/views.png)
  - Blog
    - Admin.py - [view](/readme/media/test/python/blog/admin.png)
    - Apps.py - [view](/readme/media/test/python/blog/apps.png)
    - Forms.py - [view](/readme/media/test/python/blog/forms.png)
    - Models.py - [view](/readme/media/test/python/blog/models.png)
    - Urls.py - [view](/readme/media/test/python/blog/urls.png)
    - Views.py - [view](/readme/media/test/python/blog/views.png)
    - Widgets.py - [view](/readme/media/test/python/blog/widgets.png)
  - Home
    - Apps.py - [view](/readme/media/test/python/home/apps.png)
    - Urls.py - [view](/readme/media/test/python/home/urls.png)
    - Views.py - [view](/readme/media/test/python/home/views.png)
  - Reviews
    - Admin.py - [view](/readme/media/test/python/reviews/admin.png)
    - Apps.py - [view](/readme/media/test/python/reviews/apps.png)
    - Forms.py - [view](/readme/media/test/python/reviews/forms.png)
    - Models.py - [view](/readme/media/test/python/reviews/models.png)
    - Urls.py - [view](/readme/media/test/python/reviews/urls.png)
    - Views.py - [view](/readme/media/test/python/reviews/views.png)

- Lighthouse
  - Add Products Page - [view](/readme/media/test/lighthouse/add-product.png)
  - Edit Products Page - [view](/readme/media/test/lighthouse/edit-product.png)
  - Checkout Success Page - [view](/readme/media/test/lighthouse/checkout-success.png)
  - Checkout Page - [view](/readme/media/test/lighthouse/checkout.png)
  - Bag Page - [view](/readme/media/test/lighthouse/bag.png)
  - Order History Page - [view](/readme/media/test/lighthouse/order-history.png)
  - Login Page - [view](/readme/media/test/lighthouse/login.png)
  - All Products Page - [view](/readme/media/test/lighthouse/all-products.png)
  - Single Products Page - [view](/readme/media/test/lighthouse/single-product.png)
  - Profile Page - [view](/readme/media/test/lighthouse/profile.png)
  - Sign Up Page - [view](/readme/media/test/lighthouse/sign-up.png)
  - Home Page - [view](/readme/media/test/lighthouse/homepage.png)
  - Add Blog Page - [view](/readme/media/test/lighthouse/add-blog.png)
  - Single Blog Page - [view](/readme/media/test/lighthouse/single-blog.png)
  - All Blog Page - [view](/readme/media/test/lighthouse/all-blog.png)

[Back to contents](#contents)

## **Accessibility**

[Back to contents](#contents)

---

## **Responsive and Browsers**

[Back to contents](#contents)

---