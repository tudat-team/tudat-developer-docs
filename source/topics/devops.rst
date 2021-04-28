
Development Operations
======================

DevOps is a set of practices that combines software development (Dev) and
IT operations (Ops) :cite:p:`wiki:DevOps`. Tudat relies on open
source solutions for development; GitHub for its hosted version control
system (VCS), :ref:`Conda` for it's package manager, and :ref:`Azure` for it's
continuous integration (CI) service.

.. graphviz::
    :align: center

    digraph G {
        conda [label = "conda", href = "#Test"];
        start [shape = Mdiamond, label = "start", href = "#Conda", target="_top"];

        subgraph cluster_0 {
        style = filled;
        color = lightgrey;
        node [style = filled,color = white];
        a0 -> a1 -> a2 -> a3;
        label = "process #1";
        }

        subgraph cluster_1 {
        node [style = filled];
        b0 -> b1 -> b2 -> b3;
        label = "process #2";
        color = blue
        }
        start -> a0;
        start -> b0;
        a1 -> b3;
        b2 -> a3;
        a3 -> a0;
        a3 -> end;
        b3 -> end;

        start [shape = Mdiamond];
    }

Test
----

.. toctree::
   :maxdepth: 2
   :caption: Topics

   devops/github
   devops/conda
   devops/azure
