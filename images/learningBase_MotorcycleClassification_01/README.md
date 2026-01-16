docker compose up -d --build

prüfen ob Dateien existieren:


ggf. ergänzen sodass container instanz weiter läuft
 && tail -f /dev/null"




# Data Provision Image – MotorcycleClassification

## Ownership
This Docker image and the contained dataset were created and assembled by **David Brockmeyer and Alexander Breuer**  
as part of an academic project at the **University of Potsdam**.

## Academic Context
This image was created within the course

> **“M. Grum: Advanced AI-based Application Systems”**

offered by the

> **Junior Chair for Business Information Science,  
> esp. AI-based Application Systems,  
> University of Potsdam**

The image serves exclusively academic, non-commercial purposes in the context of this course.

## Purpose of the Image
This Docker image is a **data provision image**.  
It does not execute any application logic and does not contain a running service.

Its sole purpose is to provide application-relevant data files at predefined paths inside the container filesystem, so that they can be mounted into an external Docker volume and consumed by downstream AI components (e.g. training, validation, or activation pipelines).

The concrete internal directory structure reflects the requirements of the corresponding AI application implementation.

## Data Origin
The contained dataset was **scraped and compiled from publicly accessible web sources** related to motorcycle classification and visual vehicle data.

The data collection process was conducted for **educational and research purposes only**.  
No personal data was collected.  
The dataset was not enriched with proprietary or restricted information.

Any trademarks, product names, or brand references remain the property of their respective owners.

## Dataset Organization
The internal dataset organization depends on the AI application pipeline and is therefore intentionally minimal.

Depending on the image variant, data is provided under paths such as:

- `/tmp/learningBase/train/`
- `/tmp/learningBase/validation/`
- `/tmp/activationBase/`

The exact structure is aligned with the consuming AI system and is not intended as a general-purpose dataset layout.

## Licensing
This Docker image and its contents are published under the terms of the

> **GNU Affero General Public License v3.0 (AGPL-3.0)**

By using this image, you agree to comply with the obligations of the AGPL-3.0 license.  
The license text applies to both the image configuration and the provided dataset, unless stated otherwise by upstream data sources.

## Technical Notes
- Base image: `busybox`
- This image is designed to be used together with an external Docker volume named `ai_system`
- Typical usage mounts the internal `/tmp` directory to the external volume via:

```bash
docker volume create ai_system
```

- The files in the volume in the directory /tmp can be seen via the command:

```bash
docker run --rm -v ai_system:/tmp busybox sh -c "find /tmp -maxdepth 6 -type f -print | sort"
```

- Image functionality can be tested using an image-specific `docker-compose.yml` file

```bash
docker compose up -d --build
```


## Docker Hub
This image is published on Docker Hub and can be pulled using:

```bash
docker pull <dockerhub-username>/<image-name>
```


