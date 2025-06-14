# Disclaimer
Fork is meant to be an easy way for me to keep this package using cvcuda-cu12 & cupy within the NGC 25.04 Docker Build. Also is being used as a submodule for my fork of deepface. None of my changes will be groundbreaking, so if you feel included to do a citation, please cite the original package maintainer :).

## Citation

If you use this library implementation for your research or projects, please consider using this cite:

```
@software{ivan_de_paz_centeno_2024_13901378,
  author       = {Iván de Paz Centeno},
  title        = {ipazc/mtcnn: v1.0.0},
  month        = oct,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.13901378},
  url          = {https://doi.org/10.5281/zenodo.13901378}
}
```

And the original research work from Kaipeng Zhang:

```
@article{7553523,
    author={K. Zhang and Z. Zhang and Z. Li and Y. Qiao}, 
    journal={IEEE Signal Processing Letters}, 
    title={Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks}, 
    year={2016}, 
    volume={23}, 
    number={10}, 
    pages={1499-1503}, 
    keywords={Benchmark testing;Computer architecture;Convolution;Detectors;Face;Face detection;Training;Cascaded convolutional neural network (CNN);face alignment;face detection}, 
    doi={10.1109/LSP.2016.2603342}, 
    ISSN={1070-9908}, 
    month={Oct}
}
```

You may also reference the original GitHub repository that this project was based on (including the networks weights):  
[Original MTCNN Implementation by Kaipeng Zhang](https://github.com/kpzhang93/MTCNN_face_detection_alignment/tree/master/code)

And the FaceNet's implementation that served as inspiration:
[Facenet's MTCNN implementation](https://github.com/davidsandberg/facenet/tree/master/src/align)


## About the Author

This project is developed and maintained by [Iván de Paz Centeno](https://ipazc.com), with the goal of standardizing face detection and providing an easy-to-use framework to help the research community push the boundaries of AI knowledge.

If you find this project useful, please consider supporting it through GitHub Sponsors. Your support will help cover costs related to improving the codebase, adding new features, and providing better documentation.

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-brightgreen)](https://github.com/sponsors/ipazc)


## Acknowledgments

This project has evolved over time with contributions from multiple developers. While the current codebase has been completely rewritten, we acknowledge and appreciate the valuable input and collaboration from past contributors.

A special thanks to everyone who has submitted pull requests, reported issues, or provided feedback to make this project better. 

For a full list of contributors, please visit the [GitHub contributors page](https://github.com/ipazc/mtcnn/graphs/contributors).


## License

This project is licensed under the [MIT License](LICENSE).
