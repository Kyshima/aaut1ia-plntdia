import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextileComponent } from './textile.component';

describe('TextilComponent', () => {
  let component: TextileComponent;
  let fixture: ComponentFixture<TextileComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TextileComponent]
    });
    fixture = TestBed.createComponent(TextileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
