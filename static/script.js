// Function to handle form submission for adding a user
document.getElementById('addUserForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Gather form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    // Send POST request to add user
    axios.post('http://localhost:5000/users', {
        name: name,
        email: email,
        phone_number: phone,
        address: { some: 'address' }
    })
        .then(function (response) {
            console.log(response.data); // Log the response for debugging
            loadUsers(); // Refresh user list
        })
        .catch(function (error) {
            console.error(error);
        });
});

// Function to load and display user data
function loadUsers() {
    axios.get('http://localhost:5000/users')
        .then(function (response) {
            const userList = document.getElementById('userList');
            userList.innerHTML = ''; // Clear previous user list

            response.data.data.forEach(function (user) {
                const div = document.createElement('div');
                div.classList.add('uk-margin', 'uk-card', 'uk-width-1-1', 'uk-card-default', 'uk-card-body');

                const name = document.createElement('h3');
                name.classList.add('uk-card-title');
                name.textContent = user.name;

                div.appendChild(name);



                // Create form and button for ordering a kit
                const orderForm = document.createElement('form');
                const sequencingTypeInput = document.createElement('select');
                sequencingTypeInput.innerHTML = '<option value="whole-exome-sequencing">Whole Exome Sequencing</option><option value="whole-genome-sequencing">Whole Genome Sequencing</option>';
                const orderButton = document.createElement('button');
                orderButton.textContent = 'Order Kit';

                orderForm.addEventListener('submit', function (event) {
                    event.preventDefault();

                    const sequencingType = sequencingTypeInput.value;

                    axios.post('http://localhost:5000/order', {
                        user_id: user.id,
                        sequencing_type: sequencingType,
                        shipping_info: { some: 'info' }
                    })
                        .then(function (response) {
                            console.log(response.data);
                            let response_text = '';

                            if (response.data.order_id == null) {
                                response_text = 'Order failed: ' + response.data.message;
                            } else {
                                response_text = 'Order placed successfully: ' + response.data.order_id;
                                if (response.data.notification_response) {
                                    response_text += ' Notification server response: ' + response.data.notification_response;
                                }
                            }
                            alert(response_text);
                            loadUsers(); // Refresh user list
                        })
                        .catch(function (error) {
                            console.error(error);
                        });
                });

                orderForm.appendChild(sequencingTypeInput);
                orderForm.appendChild(orderButton);
                div.appendChild(orderForm);

                // Display orders if available
                if (user.orders && user.orders.length > 0) {
                    user.orders.forEach(function (order) {
                        const orderCard = document.createElement('div');
                        orderCard.classList.add('uk-margin-bottom');
                        orderCard.style.border = '1px solid grey'; // Add inline CSS for border
                        orderCard.style.padding = '10px'; // Add inline CSS for padding

                        const orderID = document.createElement('div');
                        orderID.textContent = 'Order ID: ' + order.id;

                        const orderType = document.createElement('div');
                        orderType.textContent = 'Type: ' + order.sequencing_type;

                        orderCard.appendChild(orderID);
                        orderCard.appendChild(orderType);
                        div.appendChild(orderCard);
                    });
                }


                userList.appendChild(div);
            });
        })
        .catch(function (error) {
            console.error(error);
        });
}
// Load users on page load
loadUsers();