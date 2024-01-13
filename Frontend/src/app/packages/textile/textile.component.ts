import { Component } from '@angular/core';
import {TextileService} from "../../services/textile.service";
import {Textile} from "./textile";

@Component({
  selector: 'app-textil',
  templateUrl: './textile.component.html',
  styleUrls: ['./textile.component.css']
})
export class TextileComponent {

  constructor(private textileService: TextileService) {
  }

  responseData: any = '';

  selectedEngine: string = '';
  selectedDelicate: string = '';
  selectedBig: string = '';
  showDelicate: boolean = false;
  showBig: boolean = false;
  showMeasurements: boolean = false;
  showBudget: boolean = false;

  heightInput: string = '';
  widthInput: string = '';
  lengthInput: string = '';
  budgetInput: string = '';
  unitsInput: string = '';

  onEngineChange() {
    this.showDelicate = this.selectedEngine !== '';
    this.showMeasurements = this.selectedEngine == 'java';
    this.showBudget = this.selectedEngine == 'java';
  }

  onDelicateChange() {
    this.showBig = this.selectedDelicate == 'no';
    this.selectedBig = '';
  }

  isSubmitButtonEnabled() {
    const isJavaEngine = this.selectedEngine === 'java';
    const isPrologEngine = this.selectedEngine === 'prolog';
    const isDelicate = this.selectedDelicate === 'yes';

    if (isJavaEngine) {
      if (isDelicate) {
        return (
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      } else {
        return (
          this.selectedDelicate !== '' &&
          this.selectedBig !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }
    } else if (isPrologEngine) {
      if (isDelicate) {
        return (
          this.isUnitsFilled()
        );
      } else {
        return(
          this.selectedDelicate !== '' &&
          this.selectedBig !== '' &&
          this.isUnitsFilled()
        );
      }
    }
    return false;
  }


  areMeasurementsFilled() {
    return (
      this.heightInput !== '' &&
      this.widthInput !== '' &&
      this.lengthInput !== ''
    );
  }

  isUnitsFilled() {
    return this.unitsInput !== '';
  }

  isBudgetFilled() {
    return this.budgetInput !== '';
  }

  submitForm() {

    let engine = this.selectedEngine;
    let category = "textiles";
    let delicate;
    let big;
    let units = parseInt(this.unitsInput);
    let length = parseFloat(this.lengthInput);
    let width = parseFloat(this.widthInput);
    let height = parseFloat(this.heightInput);
    let budget = parseFloat(this.budgetInput);

    delicate = this.selectedDelicate === 'yes';
    big = this.selectedBig === 'yes';

    if (engine === 'java') {
      let textile = new Textile(category, delicate, big, units, length, width, height, budget);
      this.textileService.postTextileJava(textile).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
      });
    } else if (engine === 'prolog') {
      let textile = new Textile(category, delicate, big, units);
      this.textileService.postTextileProlog(textile).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
      });
    }
  }

  resizeAnswer() {
    // @ts-ignore
    document.getElementById("response_div").style.height = "80%";
  }

  resizeAnswerJava() {
    // @ts-ignore
    document.getElementById("response_div").style.height = "35%";
  }

}
