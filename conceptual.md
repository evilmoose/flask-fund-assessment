### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript? Python is a general-purpose language known for readability and simplicity, while JavaScript is primarily used for web development. Python emphasizes code readability and uses indentation, while JavaScript has C-style syntax with curly braces. Python is typically executed on the server-side, while JavaScript runs in web browsers and also on the server-side with Node.js. Python has a broad range of libraries and is used in various domains, while JavaScript has a strong ecosystem for web development.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?

- What is an integration test?

- What is the role of web application framework, like Flask?

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask? 
To collect data from the query string using Flask, you can access the request object and use its args attribute. The args attribute contains a dictionary of the parsed query string parameters.

- How do you collect data from the body of the request using Flask? To collect data from the body of a request using Flask, you can access the request object and use its methods to retrieve the data based on the request's content type.

- What is a cookie and what kinds of things are they commonly used for? A cookie is a small data file stored by a website on a user's browser. It is used to remember information about the user's session, like login details, preferences, items in a shopping cart, or analytics tracking data.

- What is the session object in Flask? The session object in Flask is a built-in feature for storing user-specific data across requests. It securely stores information like login details or user preferences using encrypted cookies.

- What does Flask's `jsonify()` do? Flask's jsonify() function converts Python objects into JSON-formatted responses, making it easier to create JSON responses in Flask.
