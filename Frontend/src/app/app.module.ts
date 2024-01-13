import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {FormsModule} from "@angular/forms";
import {CosmeticsComponent} from './packages/cosmetics/cosmetics.component';
import {EletronicsComponent} from './packages/eletronics/eletronics.component';
import {FoodComponent} from './packages/food/food.component';
import {FurnitureComponent} from './packages/furniture/furniture.component';
import {HealthComponent} from './packages/health/health.component';
import {TextileComponent} from './packages/textile/textile.component';
import {CropsComponent} from './crops/crops.component';
import {PlanComponent} from './crops/plan/plan.component';
import {PredictComponent} from './crops/predict/predict.component';
import {HttpClientModule} from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    CosmeticsComponent,
    EletronicsComponent,
    FoodComponent,
    FurnitureComponent,
    HealthComponent,
    TextileComponent,
    CropsComponent,
    PlanComponent,
    PredictComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
