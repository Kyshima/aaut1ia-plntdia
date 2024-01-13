import {Component} from '@angular/core';
import {Health} from "./health";
import {HealthService} from "../../services/health.service";

@Component({
  selector: 'app-health',
  templateUrl: './health.component.html',
  styleUrls: ['./health.component.css']
})
export class HealthComponent {

  constructor(private healthService: HealthService) {
  }

  responseData: any = '';

  selectedEngine: string = '';
  selectedSubcategory: string = '';
  selectedFragile: string = '';
  selectedPhysicalState: string = '';
  selectedTemperature: string = '';
  showSubcategory: boolean = false;
  showPhysicalState: boolean = false;
  showFragile: boolean = false;
  showTemperature: boolean = false;
  showMeasurements: boolean = false;
  showBudget: boolean = false;

  heightInput: string = '';
  widthInput: string = '';
  lengthInput: string = '';
  budgetInput: string = '';
  unitsInput: string = '';

  onEngineChange() {
    this.showSubcategory = this.selectedEngine !== '';
    this.showMeasurements = this.selectedEngine == 'java';
    this.showBudget = this.selectedEngine == 'java';
  }

  onSubcategoryChange() {
    this.showPhysicalState = this.selectedSubcategory !== '';

    this.selectedTemperature = '';
    this.showTemperature = false;

    this.selectedFragile = '';
    this.showFragile = false;

    this.selectedPhysicalState = '';
  }

  onPhysicalStateChange() {
    this.showTemperature = this.selectedSubcategory == 'medicine'
      && this.selectedPhysicalState !== '';
  }

  onTemperatureChange() {
    this.showFragile = this.selectedSubcategory == 'medicine'
      && this.selectedTemperature !== '';
  }

  isSubmitButtonEnabled() {
    const isJavaEngine = this.selectedEngine === 'java';
    const isPrologEngine = this.selectedEngine === 'prolog';
    const isMedicineSubcategory = this.selectedSubcategory === 'medicine';
    const isFirstAidOrHygieneSubcategory = this.selectedSubcategory === 'firstAid' || this.selectedSubcategory === 'hygieneProduct';

    if (isJavaEngine) {
      if (isMedicineSubcategory) {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedTemperature !== '' &&
          this.selectedFragile !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      } else if (isFirstAidOrHygieneSubcategory) {
        return (
          this.selectedPhysicalState !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }
    } else if (isPrologEngine) {
      if (isMedicineSubcategory) {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedTemperature !== '' &&
          this.selectedFragile !== '' &&
          this.isUnitsFilled()
        );
      } else if (isFirstAidOrHygieneSubcategory) {
        return this.selectedPhysicalState !== '' && this.isUnitsFilled();
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
    let category = "health";
    let medicine;
    let first_aid;
    let hygiene;
    let liquid;
    let temp_friendly;
    let fragile;
    let units = parseInt(this.unitsInput);
    let length = parseFloat(this.lengthInput);
    let width = parseFloat(this.widthInput);
    let height = parseFloat(this.heightInput);
    let budget = parseFloat(this.budgetInput);

    medicine = this.selectedSubcategory === 'medicine';
    first_aid = this.selectedSubcategory === 'firstAid';
    hygiene = this.selectedSubcategory === 'hygieneProduct';
    liquid = this.selectedPhysicalState === 'liquid';
    temp_friendly = this.selectedTemperature === 'yes';
    fragile = this.selectedFragile === 'yes';

    if (engine === 'java') {
      let health = new Health(category, medicine, first_aid, hygiene, liquid, temp_friendly, fragile, units, length, width, height, budget);
      this.healthService.postHealthJava(health).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
        console.log(this.responseData);
      });
    } else if (engine === 'prolog') {
      let health = new Health(category, medicine, first_aid, hygiene, liquid, temp_friendly, fragile, units);
      this.healthService.postHealthProlog(health).subscribe((data) => {
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
