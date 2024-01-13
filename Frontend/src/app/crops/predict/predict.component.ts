import {Component, OnInit, OnDestroy  } from '@angular/core';
import {Predict} from "./predict";
import { PredictService } from 'src/app/services/predict.service';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit, OnDestroy  {

  constructor(private predictService: PredictService) {
  }

  responseData: any = '';

  selectState: string="";
  selectCrop: string="";
  pa1: number = 0;
  pa2: number = 0;
  pa3: number = 0;
  pa4: number = 0;
  prod1: number = 0;
  prod2: number = 0;
  prod3: number = 0;

  ngOnInit(): void {
    // This function will run when the component is initialized
    
  }

  ngOnDestroy(): void {
    // This function will run when the component is about to be destroyed
    
  }

  isSubmitButtonEnabledPredict() {
    return this.selectState !="" && this.selectCrop !="" && this.pa1 != 0 && this.pa2 != 0 && this.pa3 != 0 && this.pa4 != 0 && this.prod1 != 0 && this.prod2 != 0 && this.prod3 != 0;
  }

  submitFormPredict() {
    console.log("submit");

    if(this.isSubmitButtonEnabledPredict()) {
      let predict = new Predict(this.selectState, this.selectCrop, this.pa1, this.prod1, this.pa2, this.prod2, this.pa3, this.prod3, this.pa4);
      this.predictService.postPredict(predict).subscribe((data) => {
        this.responseData = JSON.parse(JSON.stringify(data));
      });
    }
  }

}
