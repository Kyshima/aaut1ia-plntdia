import {Component} from '@angular/core';
import {Eletronics} from "./eletronics";
import {EletronicsService} from "../../services/eletronics.service";

@Component({
    selector: 'app-eletronics',
    templateUrl: './eletronics.component.html',
    styleUrls: ['./eletronics.component.css']
})
export class EletronicsComponent {

    constructor(private eletronicsService: EletronicsService) {
    }

    responseData: any = '';

    selectedEngine: string = '';
    selectedSize: string = '';
    selectedVisibility: string = '';
    selectedResistant: string = '';
    selectedHeavy: string = '';
    selectedFragile: string = '';
    showSize: boolean = false;
    showVisibility: boolean = false;
    showResistant: boolean = false;
    showHeavy: boolean = false;
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
        this.showFragile = this.selectedSize == 'small';
        this.showHeavy = this.selectedSize == 'big';
        this.showResistant = this.selectedFragile == 'yes' && this.selectedSize == 'small';
        this.showVisibility = this.selectedFragile == 'no' && this.selectedSize == 'small';

        this.selectedResistant = '';
        this.selectedVisibility = '';
        this.selectedFragile = '';
        this.selectedHeavy = '';
    }

    onHeavyChange() {
        this.showFragile = this.selectedHeavy == 'heavy' && this.selectedSize == 'big';
        this.selectedFragile = '';
    }

    onFragileChange() {
        this.showResistant = this.selectedFragile == 'yes' && this.selectedSize == 'small';
        this.showVisibility = this.selectedFragile == 'no' && this.selectedSize == 'small';
        this.selectedResistant = '';
        this.selectedVisibility = '';
    }

    isSubmitButtonEnabled() {
        const isJavaEngine = this.selectedEngine === 'java';
        const isPrologEngine = this.selectedEngine === 'prolog';
        const isSizeBig = this.selectedSize === 'big';
        const isSizeSmall = this.selectedSize === 'small';
        const isFragileYes = this.selectedFragile === 'yes';
        const isFragileNo = this.selectedFragile === 'no';
        const isHeavy = this.selectedHeavy === 'heavy';
        const isLight = this.selectedHeavy === 'light';


        if (isJavaEngine) {
            if (isSizeSmall && isFragileYes) {
                return (
                    this.selectedResistant !== '' &&
                    this.areMeasurementsFilled() &&
                    this.isBudgetFilled() &&
                    this.isUnitsFilled()
                );
            } else if (isSizeSmall && isFragileNo) {
                return (
                    this.selectedVisibility !== '' &&
                    this.areMeasurementsFilled() &&
                    this.isBudgetFilled() &&
                    this.isUnitsFilled()
                );
            }
            else if (isSizeBig && isHeavy) {
                return (
                    this.selectedFragile !== '' &&
                    this.areMeasurementsFilled() &&
                    this.isBudgetFilled() &&
                    this.isUnitsFilled()
                );
            }
            else if (isSizeBig && isLight) {
                return (
                    this.areMeasurementsFilled() &&
                    this.isBudgetFilled() &&
                    this.isUnitsFilled()
                );
            }
        } else if (isPrologEngine) {
            if (isSizeSmall && isFragileYes) {
                return (
                    this.selectedResistant !== '' &&
                    this.isUnitsFilled()
                );
            } else if (isSizeSmall && isFragileNo) {
                return (
                    this.selectedVisibility !== '' &&
                    this.isUnitsFilled()
                );
            }
            else if (isSizeBig && isHeavy) {
                return (
                    this.selectedFragile !== '' &&
                    this.isUnitsFilled()
                );
            }
            else if (isSizeBig && isLight) {
                return (
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
        let category = "electronics";
        let big;
        let fragile;
        let resistant;
        let visibility;
        let heavy;
        let units = parseInt(this.unitsInput);
        let length = parseFloat(this.lengthInput);
        let width = parseFloat(this.widthInput);
        let height = parseFloat(this.heightInput);
        let budget = parseFloat(this.budgetInput);

        big = this.selectedSize === 'big';
        resistant = this.selectedResistant === 'yes';
        visibility = this.selectedVisibility === 'yes';
        heavy = this.selectedHeavy === 'heavy';
        fragile = this.selectedFragile === 'yes';

        if (engine === 'java') {
            let eletronics = new Eletronics(category, big, fragile, resistant, visibility, heavy, units, length, width, height, budget);
            this.eletronicsService.postEletronicsJava(eletronics).subscribe((data) => {
                this.responseData = JSON.parse(JSON.stringify(data));
            });
        } else if (engine === 'prolog') {
            let eletronics = new Eletronics(category, big, fragile, resistant, visibility, heavy, units, length, width, height, budget);
            this.eletronicsService.postEletronicsProlog(eletronics).subscribe((data) => {
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
