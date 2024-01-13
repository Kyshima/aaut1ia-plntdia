import {Component, OnInit, OnDestroy  } from '@angular/core';
import { Router } from '@angular/router';
import {Packages} from "./crops";
import {PackagesService} from "../services/packages.service";

@Component({
  selector: 'app-health',
  templateUrl: './crops.component.html',
  styleUrls: ['./crops.component.css']
})

export class CropsComponent implements OnInit, OnDestroy  {

  constructor(private packagesService: PackagesService, private router: Router) {
  }

  ngOnInit(): void {
    // This function will run when the component is initialized
    
  }

  ngOnDestroy(): void {
    // This function will run when the component is about to be destroyed
    
  }

  navigateToPlan() {
    this.router.navigate(['/crops/plan']);
  }

  navigateToPredict() {
    this.router.navigate(['/crops/predict']);
  }
  



}
