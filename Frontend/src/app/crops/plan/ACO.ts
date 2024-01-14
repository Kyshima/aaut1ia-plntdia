export class ACO {

    constructor(
      public weights: number[],
      public state: string,
      public number_crops: number,
      public pheromone_initial: number,
      public pheromone_decay: number,
      public alpha: number,
      public beta: number,
      public  num_ants: number,
      public num_iterations: number,
      public temporal: boolean,
      public max_time: number,
    ) {
    }
  
  
  }