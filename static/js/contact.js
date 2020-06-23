// This function allows us to send an email through emailjs free service. 
// While making it, I was inspired by course materials, 
// specifficaly last part of "Interactive Frontend development" section.

console.log("I'm in")

function sendMail(contactForm) {
	emailjs.send("gmail", "speak", {
			"from_name": contactForm.name.value,
			"from_email": contactForm.email.value,
			"eng": contactForm.eng.value,
			"change": contactForm.change.value,
			"more": contactForm.more.value
		})
		.then(
			function (response) {
				alert("Success! Your form has been submited", response);
			},
			function (error) {
				console.log("Sending message failed! Please try again.", error);
			})
		.then(
			function redirect() {
				location.replace("index.html");
			}
		);
	return false;

}