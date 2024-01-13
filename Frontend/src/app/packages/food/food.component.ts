import {Component} from '@angular/core';
import {Food} from "./food";
import {FoodService} from "../../services/food.service";

@Component({
  selector: 'app-health',
  templateUrl: './food.component.html',
  styleUrls: ['./food.component.css']
})
export class FoodComponent {

  constructor(private foodService: FoodService) {
  }
 
  responseData: any = '';

  selectedEngine: string = '';
  selectedFragile: string = '';
  selectedPhysicalState: string = '';
  selectedBig: string = '';
  showPhysicalState: boolean = false;
  showFragile: boolean = false;
  showBig: boolean = false;
  showMeasurements: boolean = false;
  showBudget: boolean = false;

  heightInput: string = '';
  widthInput: string = '';
  lengthInput: string = '';
  budgetInput: string = '';
  unitsInput: string = '';

  onEngineChange() {
    this.showPhysicalState = this.selectedEngine !== '';
    this.showMeasurements = this.selectedEngine == 'java';
    this.showBudget = this.selectedEngine == 'java';
  }

  onPhysicalStateChange() {
    this.showFragile = this.selectedPhysicalState == 'liquid';
    this.showBig = this.selectedPhysicalState == 'solid';

    this.selectedFragile = '';
    this.selectedBig = '';
  }

  onSizeChange() {
    this.showFragile = true;
  }

  isSubmitButtonEnabled() {
    const isJavaEngine = this.selectedEngine === 'java';
    const isPrologEngine = this.selectedEngine === 'prolog';
    const isLiquid = this.selectedPhysicalState === 'liquid';

    if (isJavaEngine) {
      if(isLiquid) {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedFragile !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }else {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedBig !== '' &&
          this.selectedFragile !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }
    } else if (isPrologEngine) {
      if(isLiquid) {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedFragile !== '' &&
          this.isUnitsFilled()
        );
      }else {
        return (
          this.selectedPhysicalState !== '' &&
          this.selectedBig !== '' &&
          this.selectedFragile !== '' &&
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
    let category = "food";
    let liquid;
    let big;
    let fragile;
    let units = parseInt(this.unitsInput);
    let length = parseFloat(this.lengthInput);
    let width = parseFloat(this.widthInput);
    let height = parseFloat(this.heightInput);
    let budget = parseFloat(this.budgetInput);

    liquid = this.selectedPhysicalState === 'liquid';
    big = this.selectedBig === 'yes';
    fragile = this.selectedFragile === 'yes';

    if (engine === 'java') {
      let food = new Food(category, big, liquid, fragile, units, length, width, height, budget);
      this.foodService.postFoodJava(food).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));

      });
    } else if (engine === 'prolog') {
      let health = new Food(category, big, liquid, fragile, units);
      this.foodService.postFoodProlog(health).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
        console.log(this.responseData);
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
