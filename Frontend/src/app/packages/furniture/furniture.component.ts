import {Component} from '@angular/core';
import {Furniture} from "./furniture";
import {FurnitureService} from "../../services/furniture_service";

@Component({
  selector: 'app-health',
  templateUrl: './furniture.component.html',
  styleUrls: ['./furniture.component.css']
})
export class FurnitureComponent {

  constructor(private healthService: FurnitureService) {
  }

  responseData: any = '';

  selectedEngine: string = '';
  selectedSize: string = '';
  selectedSoldInPieces: string = '';
  selectedFragile: string = '';
  showSize: boolean = false;
  showSoldInPieces: boolean = false;
  showFragile: boolean = false;
  showMeasurements: boolean = false;
  showBudget: boolean = false;

  heightInput: string = '';
  widthInput: string = '';
  lengthInput: string = '';
  budgetInput: string = '';
  unitsInput: string = '';

  onEngineChange() {
    this.showSize = this.selectedEngine !== '';
    this.showMeasurements = this.selectedEngine == 'java';
    this.showBudget = this.selectedEngine == 'java';
  }

  onSizeChange() {
    this.showFragile = this.selectedSize === 'small';
    this.showSoldInPieces = this.selectedSize === 'big';

    this.selectedSoldInPieces = '';
    this.selectedFragile = '';
  }

  onSoldInPiecesChange() {
    this.showFragile = this.selectedSize === 'big' && this.selectedSoldInPieces === 'whole' ;

    this.selectedFragile = '';
  }

  isSubmitButtonEnabled() {
    const isJavaEngine = this.selectedEngine === 'java';
    const isPrologEngine = this.selectedEngine === 'prolog';
    const isBig = this.selectedSize === 'small';
    console.log(this.selectedSize);
    const isSold = this.selectedSoldInPieces === 'pieces';

    if (isJavaEngine) {
      if (isBig) {
        return (
          this.selectedSize !== '' &&
          this.selectedFragile !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      } else if (isSold) {
        return (
          this.selectedSize !== '' &&
          this.selectedSoldInPieces !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }else{
        return (
          this.selectedSize !== '' &&
          this.selectedFragile !== '' &&
          this.selectedSoldInPieces !== '' &&
          this.areMeasurementsFilled() &&
          this.isBudgetFilled() &&
          this.isUnitsFilled()
        );
      }
    } else if (isPrologEngine) {
      if (isBig) {
        return (
          this.selectedSize !== '' &&
          this.selectedFragile !== '' &&
          this.isUnitsFilled()
        );
      } else if (isSold) {
        return (
          this.selectedSize !== '' &&
          this.selectedSoldInPieces !== '' &&
          this.isUnitsFilled()
        );
      }else{
        return (
          this.selectedSize !== '' &&
          this.selectedFragile !== '' &&
          this.selectedSoldInPieces !== '' &&
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
    let category = "furniture";
    let big;
    let sold_in_pieces;
    let fragile;
    let units = parseInt(this.unitsInput);
    let length = parseFloat(this.lengthInput);
    let width = parseFloat(this.widthInput);
    let height = parseFloat(this.heightInput);
    let budget = parseFloat(this.budgetInput);

    big = this.selectedSize === 'big';
    sold_in_pieces = this.selectedSoldInPieces === 'pieces';
    fragile = this.selectedFragile === 'yes';

    if (engine === 'java') {
      let furniture = new Furniture(category, big, fragile, sold_in_pieces, units, length, width, height, budget);
      this.healthService.postFurnitureJava(furniture).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
      });
    } else if (engine === 'prolog') {
      let furniture = new Furniture(category, big, fragile, sold_in_pieces, units);
      this.healthService.postFurnitureProlog(furniture).subscribe((data) => {
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
