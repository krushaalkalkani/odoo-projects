odoo.define("custom_pos.inherit", function (require) {
  "use strict";
  const ProductScreen = require("point_of_sale.ProductScreen");
  const Registries = require("point_of_sale.Registries");
  var { Gui } = require("point_of_sale.Gui");
  const { _lt } = require("@web/core/l10n/translation");

  const CustomerNoteButton = (ProductScreen) =>
    class CustomerNoteButton extends ProductScreen {
      setup() {
        super.setup();
        console.log(this.env.pos);
      }
      async onClick() {
        const order = this.env.pos.get_order();
        const { confirmed, payload: inputNote } = await this.showPopup(
          "TextAreaPopup",
          {
            title: "Add Customer Comments",
            startingValue: order.get_custom_note(),
            confirmText: "Confirm",
            cancelText: "Cancel",
          }
        );
        if (confirmed) {
          order.set_custom_note(inputNote);
          console.log(order);
        }
      }
      async _onClickPay() {
        if (this.env.pos.get_order().partner == null) {
          Gui.showPopup("ErrorPopup", {
            title: _lt("Customer"),
            body: _lt(`Customer is not Selected!`),
          });
        } else {
          super._onClickPay();
        }
      }
    };
  CustomerNoteButton.template = "pos_task.CustomerNoteButton";
  Registries.Component.extend(ProductScreen, CustomerNoteButton);
});
