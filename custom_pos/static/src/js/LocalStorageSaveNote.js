odoo.define("custom_pos.LocalStorageSave", function (require) {
  "use strict";

  //   const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
  const Registries = require("point_of_sale.Registries");
  //   const { _lt } = require("@web/core/l10n/translation");
  const { Order } = require("point_of_sale.models");

  //   const { useState, useRef } = owl;

  const LocalStorageSave = (Order) =>
    class LocalStorageSave extends Order {
      constructor() {
        super(...arguments);
        this.custom_note = this.custom_note || "Blank";
      }

      export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.custom_note = this.custom_note;
        return json;
      }

      init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        this.set_custom_note(json.custom_note);
      }

      set_custom_note(custom_note) {
        this.custom_note = custom_note;
      }

      get_custom_note() {
        return this.custom_note;
      }

      export_for_printing() {
        console.log(this.partner);
        const result = super.export_for_printing(...arguments);
        if (this.get_custom_note()) {
          result.custom_note = this.get_custom_note();
        }
        return result;
      }
    };

  Registries.Model.extend(Order, LocalStorageSave);
});
