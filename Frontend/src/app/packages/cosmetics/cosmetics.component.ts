import { Component } from '@angular/core';
import {CosmeticsService} from "../../services/cosmetics.service";
import {Cosmetics} from "./cosmetics";

@Component({
  selector: 'app-cosmetics',
  templateUrl: './cosmetics.component.html',
  styleUrls: ['./cosmetics.component.css']
})
export class CosmeticsComponent {

  constructor(private cosmeticsService: CosmeticsService) {
  }

  responseData: any = '';

  selectedEngine: string = '';
  selectedFragile: string = '';
  selectedLiquid: string = '';
  selectedBig: string = '';
  showFragile: boolean = false;
  showLiquid: boolean = false;
  showBig: boolean = false;
  showMeasurements: boolean = false;
  showBudget: boolean = false;

  heightInput: string = '';
  widthInput: string = '';
  lengthInput: string = '';
  budgetInput: string = '';
  unitsInput: string = '';

  onEngineChange() {
    this.showFragile = this.selectedEngine !== '';
    this.showMeasurements = this.selectedEngine == 'java';
    this.showBudget = this.selectedEngine == 'java';
  }

  onFragileChange() {
    this.showBig = this.showLiquid = false;
    if(this.selectedFragile == 'yes') this.showLiquid = true;
    else this.showBig = true;
  }

  onLiquidChange() {
    if(this.selectedLiquid == 'no') this.showBig = true;
  }

  isSubmitButtonEnabled() {
    const isJavaEngine = this.selectedEngine === 'java';
    const isPrologEngine = this.selectedEngine === 'prolog';
    const isFragile = this.selectedFragile === 'yes';
    const isLiquid = this.selectedLiquid === 'yes';

    if (isJavaEngine) {
      if (isFragile) {
        if (!isLiquid) {
          return (
            this.selectedFragile !== '' &&
            this.selectedLiquid !== '' &&
            this.selectedBig !== '' &&
            this.areMeasurementsFilled() &&
            this.isBudgetFilled() &&
            this.isUnitsFilled()
          );
        } else {
          return (
            this.selectedFragile !== '' &&
            this.selectedLiquid !== '' &&
            this.areMeasurementsFilled() &&
            this.isBudgetFilled() &&
            this.isUnitsFilled()
          );
        }
      } else {
        return (
        this.selectedFragile !== '' &&
        this.selectedBig !== '' &&
        this.areMeasurementsFilled() &&
        this.isBudgetFilled() &&
        this.isUnitsFilled()
        );
      }
      } else if (isPrologEngine) {
      if (isFragile) {
        if (!isLiquid) {
          return (
            this.selectedFragile !== '' &&
            this.selectedLiquid !== '' &&
            this.selectedBig !== '' &&
            this.isUnitsFilled()
          );
        } else {
          return (
            this.selectedFragile !== '' &&
            this.selectedLiquid !== '' &&
            this.isUnitsFilled()
          );
        }
      } else {
        return(
        this.selectedFragile !== '' &&
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
    let category = "cosmetics";
    let fragile;
    let liquid;
    let big;
    let units = parseInt(this.unitsInput);
    let length = parseFloat(this.lengthInput);
    let width = parseFloat(this.widthInput);
    let height = parseFloat(this.heightInput);
    let budget = parseFloat(this.budgetInput);

    fragile = this.selectedFragile === 'yes';
    liquid = this.selectedLiquid === 'yes';
    big = this.selectedBig === 'yes';

    if (engine === 'java') {
      let cosmetics = new Cosmetics(category, fragile, liquid, big, units, length, width, height, budget);
      this.cosmeticsService.postCosmeticsJava(cosmetics).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
      });
    } else if (engine === 'prolog') {
      let cosmetics = new Cosmetics(category, fragile, liquid, big, units);
      this.cosmeticsService.postCosmeticsProlog(cosmetics).subscribe((data) => {
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
