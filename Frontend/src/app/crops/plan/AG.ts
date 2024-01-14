export class AG {

  constructor(
    public weights: number[],
    public state: string,
    public number_genes: number,
    public population_size: number,
    public max_generations_without_improvement: number,
    public mutation_rate: number,
    public temporal: boolean,
    public max_time: number,
  ) {
  }

}
