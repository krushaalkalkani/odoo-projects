odoo.define("custom_pos.CustomerNotePopup", function (require) {
  "use strict";

  const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
  const Registries = require("point_of_sale.Registries");
  const { _lt } = require("@web/core/l10n/translation");
  // const { Order } = require("point_of_sale.models");

  const { useState, useRef } = owl;

  class CustomerNotePopup extends AbstractAwaitablePopup {
    setup() {
      super.setup();
      this.custom_note = useRef("custom_note");
      this.current_note_state = useState({
        order_custom_note_: this.props.initialNumber,
      });
      this.custom_note = useState({
        error: "############### -Hello there are error!- ################",
      });
    }

    getPayload() {
      console.log(this.current_note_state);
      return this.current_note_state.order_custom_note_;
    }
  }

  CustomerNotePopup.template = "custom_pos.CustomerNotePopup";
  CustomerNotePopup.defaultProps = {
    cancelText: _lt("Cancel"),
    title: _lt("Order Note"),
    save: _lt("Save"),
  };

  Registries.Component.add(CustomerNotePopup);
});
