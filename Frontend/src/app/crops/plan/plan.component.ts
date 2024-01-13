import {Component, OnInit, OnDestroy  } from '@angular/core';
import {Plan} from "./plan";
import {PlanService} from "../../services/plan.service";

@Component({
  selector: 'app-plan',
  templateUrl: './plan.component.html',
  styleUrls: ['./plan.component.css']
})
export class PlanComponent implements OnInit, OnDestroy  {

  constructor(private planService: PlanService) {
  }

  stateInputACO: string = '';
  prodCostACO: number = 0;
  cultCostACO: number = 0;
  operCostACO: number = 0;
  fixedCostACO: number = 0;
  numResultsACO: number = 0;

  stateInputAG: string = '';
  prodCostAG: number = 0;
  cultCostAG: number = 0;
  operCostAG: number = 0;
  fixedCostAG: number = 0;
  numResultsAG: number = 0;

  canSubmitCostACO: boolean = false;
  canSubmitCostAG: boolean = false;

  ngOnInit(): void {
    // This function will run when the component is initialized
    
  }

  ngOnDestroy(): void {
    // This function will run when the component is about to be destroyed
    
  }

  
  isSubmitButtonEnabledACO() {
    return this.stateInputACO !="" && this.prodCostACO != 0 && this.cultCostACO != 0 && this.operCostACO != 0 && this.fixedCostACO != 0 && this.numResultsACO != 0;
  }

  isSubmitButtonEnabledAG() {
    return this.stateInputAG !="" && this.prodCostAG != 0 && this.cultCostAG != 0 && this.operCostAG != 0 && this.fixedCostAG != 0 && this.numResultsAG != 0;
  }

  onCostACOChange() {
    if((this.prodCostACO + this.cultCostACO + this.operCostACO + this.fixedCostACO) > 1) {
      this.canSubmitCostACO = false;
      alert("The sum of the cost percentages can't be bigger than 1!");
    }else this.canSubmitCostACO = true;
  }

  onCostAGChange() {
    if((this.prodCostAG + this.cultCostAG + this.operCostAG + this.fixedCostAG) > 1) {
      this.canSubmitCostAG = false;
      alert("The sum of the cost percentages can't be bigger than 1!");
    }else this.canSubmitCostAG = true;
  }

  submitFormAG() {
    console.log("submit");

    // let food = new Food(category, big, liquid, fragile, units, length, width, height, budget);
    // this.foodService.postFoodJava(food).subscribe((data) => {
    //   this.responseData = JSON.parse(JSON.stringify(data));

    // });
  }

  submitFormACO() {
    console.log("submit");
  }

}
