import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {CropsComponent} from "./crops/crops.component";
import { PredictComponent } from './crops/predict/predict.component';
import { PlanComponent } from './crops/plan/plan.component';

const routes: Routes = [
  { path: 'crops', component: CropsComponent },
  { path: 'crops/plan', component: PlanComponent },
  { path: 'crops/predict', component: PredictComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
