import {Component, OnInit, OnDestroy  } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-health',
  templateUrl: './crops.component.html',
  styleUrls: ['./crops.component.css']
})

export class CropsComponent implements OnInit, OnDestroy  {

  constructor(private router: Router) {
  }

  ngOnInit(): void {
    
  }

  ngOnDestroy(): void {
    
  }

  navigateToPlan() {
    this.router.navigate(['/crops/plan']);
  }

  navigateToPredict() {
    this.router.navigate(['/crops/predict']);
  }
  
}
