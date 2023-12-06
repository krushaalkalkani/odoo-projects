/**@odoo-modules */
import { PosGlobalState } from "point_of_sale.models";
import Registries from "point_of_sale.Registries";

const PosGlobalValue = (PosGlobalState) =>
  class extends PosGlobalState {
    async _processData(loadedData) {
      await super._processData(...arguments);
      this.sale_location = loadedData["sale.location"];
    }
  };

Registries.Model.extend(PosGlobalState, PosGlobalValue);
