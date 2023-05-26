# Roadmap

## Block Diagram

(to be updated as we actually work on the thing)

```{graphviz}
digraph {
  rankdir=LR
    
  subgraph cluster_io {
      label="io module"
      io
      eeglab[label="eeglab"]
      nwb
      
      eeglab -> io
      nwb -> io
  }
  
  subgraph cluster_models {
      rankdir="TB"
      label="models"
      
      model
      sleep
      eeg_timeseries
      sleep_stages
      
      model -> sleep
      sleep -> eeg_timeseries
      sleep -> sleep_stages
  }
  

  subgraph cluster_analysis {
      label="analysis"
      
      analysis
      random_forest
      analysis -> random_forest
      
  }
  
  subgraph cluster_viz {
      label="Visualization"
      
      viz
      classification_plot
      
      viz -> classification_plot
  }
  
  io -> model
  analysis -> viz
  model -> analysis
  

}
```

## Desired functionality

### Top-level

Analyzing sleep data! Specifically, automatically assigning sleep phases from eeg recordings

Understand how memory consolidation is affected by sleep

### Features

- i/o
  - Load [EEGLab data](#sleep_analysis.io.eeglab)
- Analysis
  - Detect sharp wave ripples
  - Analyze sharp wave ripples as it relates to low-dimensional neural manifolds