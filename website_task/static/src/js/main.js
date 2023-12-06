/** @odoo-module **/
import publicWidget from "web.public.widget";

publicWidget.registry.FormSubmit = publicWidget.Widget.extend({
  selector: "#custom_form",

  events: {
    "click #submit": "submit",
  },

  submit(e) {
    e.preventDefault();
    var self = this;

    var popup = self.$el.find(".custom-login-signup-modal");
    console.log(self.getSession().user_id);
    if (!self.getSession().user_id) {
      // Show the login and sign-up modal
      console.log(self.$el);
      popup.modal("show");

      // Handle login button click
      self.$(".login-button").on("click", function () {
        // Redirect to the login page
        window.location.href = "/web/login";
      });

      // Handle sign-up button click
      self.$(".signup-button").on("click", function () {
        // Redirect to the sign-up page or your custom registration page
        window.location.href = "/web/signup"; // Update with your signup URL
      });
      console.log(self.$(".close"));
      self.$(".close").on("click", function () {
        popup.modal("hide");
      });
    }
  },
});
