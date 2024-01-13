import {Component, OnInit, OnDestroy  } from '@angular/core';
import {Predict} from "./predict";

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit, OnDestroy  {

  constructor() {
  }

  select1: string="";
  select2: string="";
  input1: number = 0;
  input2: number = 0;
  input3: number = 0;
  input4: number = 0;
  input5: number = 0;
  input6: number = 0;
  input7: number = 0;

  ngOnInit(): void {
    // This function will run when the component is initialized
    
  }

  ngOnDestroy(): void {
    // This function will run when the component is about to be destroyed
    
  }

 


}
