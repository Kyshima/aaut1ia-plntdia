import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CosmeticsComponent } from './packages/cosmetics/cosmetics.component';
import {EletronicsComponent} from "./packages/eletronics/eletronics.component";
import {FurnitureComponent} from "./packages/furniture/furniture.component";
import {FoodComponent} from "./packages/food/food.component";
import {HealthComponent} from "./packages/health/health.component";
import {TextileComponent} from "./packages/textile/textile.component";
import {PackagesComponent} from "./packages/packages.component";
import {CropsComponent} from "./crops/crops.component";
import { PredictComponent } from './crops/predict/predict.component';
import { PlanComponent } from './crops/plan/plan.component';

const routes: Routes = [
  { path: 'packages', component: PackagesComponent },
  { path: 'cosmetics', component: CosmeticsComponent },
  { path: 'eletronics', component: EletronicsComponent },
  { path: 'furniture', component: FurnitureComponent },
  { path: 'food', component: FoodComponent },
  { path: 'health', component: HealthComponent },
  { path: 'textil', component: TextileComponent },
  { path: 'crops', component: CropsComponent },
  { path: 'crops/plan', component: PlanComponent },
  { path: 'crops/predict', component: PredictComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
