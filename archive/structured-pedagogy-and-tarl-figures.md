# Smart Buys: Structured Pedagogy and Mentions

## Sample Flow (From `0.35 Summary Statistics.do`)

```mermaid
flowchart TD
  A["1,618 Excel URLs (UNESCO database)"] --> B["1,008 PDFs present in local folder (892 unique URLs)"]
  A --> N0["608 URLs not downloaded as PDFs<br/>• 243 HTML page, no PDF found<br/>• 102 Invalid/non-HTTP URL<br/>• 91 Connection error<br/>• 68 Unknown/blank<br/>• 34 Timeout<br/>• 27 Invalid schema (httpss/)<br/>• 24 SSL error<br/>• 12 Non-PDF content type<br/>• 4 Runtime error<br/>• 2 Other error<br/>• 1 Saved HTML (not PDF)"]
  B --> C["868 PDFs are OCR-readable"]
  C --> D["English or English-accessible"]
  D --> E["528 English-language PDFs (used in analysis)"]
  D --> F["48 foreign-language PDFs with an English copy"]
  E --> G["Sample detail: 414 country-year observations"]
  C --> H["Foreign language with no English copy"]
  H --> I["292 PDFs without an English version"]
  I --> J["143 French only"]
  I --> K["60 Spanish only"]
  I --> L["89 other languages"]
  E -.-> M["Used in nep_data_filtered.dta"]
```

## Structured Pedagogy Figures (Smart Buys)

![Structured pedagogy by income (count)](assets/figures/bb_structped_income_count.png)

![Structured pedagogy by income (percent)](assets/figures/bb_structped_income_pct.png)

![Structured pedagogy by region (count)](assets/figures/bb_structped_region_count.png)

![Structured pedagogy by region (percent)](assets/figures/bb_structped_region_pct.png)

## TaRL Figures

![TaRL targeted instruction by income (count)](assets/figures/tarl_targeted_income_count.png)

![TaRL targeted instruction by income (percent)](assets/figures/tarl_targeted_income_pct.png)

![TaRL targeted instruction by region (count)](assets/figures/tarl_targeted_region_count.png)

![TaRL targeted instruction by region (percent)](assets/figures/tarl_targeted_region_pct.png)

## Mention Graphs

![Smart buys mention counts](assets/figures/bb_mention_counts.png)

![Smart buys mention percent by income](assets/figures/bb_mention_pct_by_income.png)
