import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PredictComponent } from './predict/predict.component';
import { PlanComponent } from './plan/plan.component';

const routes: Routes = [
  { path: 'crops/plan', component: PlanComponent },
  { path: 'crops/predict', component: PredictComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CropsRoutingModule { }
