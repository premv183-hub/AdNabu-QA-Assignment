Test Case 1 – Search with Valid Product Name
Steps
Open the AdNabu test store
Click on the search icon
Enter a valid product name
Press Enter
Expected Result

The relevant product should be displayed in the search results.

Test Case 2 – Search with Invalid Product Name
Steps
Open the website
Click on the search icon
Enter a random invalid product name
Press Enter
Expected Result

The application should display a “No products found” message or empty result page.

Test Case 3 – Search Using Special Characters (Edge Case)
Steps
Open the website
Click on the search icon
Enter special characters like @#$%^
Press Enter
Expected Result

The application should handle the input properly without crashing or showing any unexpected behavior.

Add to Cart Test Cases
Test Case 4 – Add Available Product to Cart Successfully
Steps
Search for an available product
Open the product page
Click on “Add to cart”
Expected Result

The selected product should be added successfully to the shopping cart.

Test Case 5 – Try Adding Sold Out Product to Cart
Steps
Search for a sold-out product
Open the product page
Try adding the product to cart
Expected Result

The application should display “Sold out” status and should not allow the product to be added to the cart.

Test Case 6 – Add Same Product Multiple Times (Edge Case)
Steps
Open an available product page
Click on “Add to cart” multiple times quickly
Expected Result

The cart quantity should update correctly without duplicate issues or application errors.