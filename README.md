<img width="1536" height="1024" alt="FanCaster Logo" src="https://github.com/user-attachments/assets/bf4cc98f-7dd5-4fea-82b6-547a82a42c55" />


# FanCaster

## AI-Powered Sports Media Operating Platform

**Transforming trusted sports data into publication-ready content with TxLINE and QVAC Local AI.**

---
One Pager: https://docs.google.com/document/d/1Pg9DjabWAj0j91QJhdpVDB_JoRR4cIAOB7e9JG4Ire4/edit?usp=sharing

Technical Documentation: https://docs.google.com/document/d/1qB3U_VMRcy_h7XJe8ZDG2hKsiYNFGbM_WADXkX9hmdw/edit?usp=sharing

PPT Deck: https://docs.google.com/presentation/d/162Zk7JL-4m3jr6sm90BiqKvmwzp_H3DXzda832_HvIE/edit?usp=sharing

Demo Video: https://youtu.be/QT06q-dNEbY


## Overview

FanCaster is an AI-powered Sports Media Operating Platform designed for sports creators, journalists, digital publishers, and media organizations.

Modern sports publishing demands instant, accurate, and engaging content. During live sporting events, creators often spend valuable time monitoring multiple sources, verifying information, understanding match context, and preparing content before they can publish.

FanCaster streamlines this entire workflow by combining trusted sports data from **TxLINE** with **QVAC Local AI** to automatically identify editorial opportunities and generate publication-ready content.

Although this project demonstrates the workflow using the FIFA World Cup, the architecture is designed to support any sport backed by structured real-time data.

---

# The Problem

Sports creators face several challenges during live events:

- Monitoring multiple sources simultaneously
- Understanding the significance of rapidly changing events
- Creating engaging content before the news cycle moves on
- Maintaining consistency across multiple publishing platforms
- Balancing speed with accuracy

By the time content is ready, the audience has often moved on.

---

# The Solution

FanCaster continuously monitors trusted sports data, detects meaningful moments, understands their editorial significance, and assists creators by generating publication-ready content within seconds.

Instead of replacing creators, FanCaster acts as an AI-powered editorial assistant that enables them to focus on storytelling rather than information gathering.

---

# Architecture

```
Sports Events
      │
      ▼
 TxLINE Sports Data
      │
      ▼
 Event Detection Engine
      │
      ▼
 Editorial Intelligence Engine
      │
      ▼
 QVAC Local AI
      │
      ▼
 Publication Ready Content
      │
      ▼
 Social Platforms
```

---

# Core Components

## TxLINE Integration

FanCaster uses TxLINE as its trusted sports data layer.

The platform consumes normalized sports data including:

- Live match events
- Fixtures
- Scores
- Competition information
- Historical match data
- Consensus betting odds

TxLINE enables FanCaster to build editorial intelligence on structured and reliable sports information.

---

## Editorial Intelligence Engine

The Editorial Intelligence Engine analyzes incoming sports events and determines:

- Story significance
- Match momentum
- Breaking news opportunities
- Context enrichment
- Editorial priority

This transforms raw sports data into meaningful publishing opportunities.

---

## QVAC Local AI

QVAC provides local AI capabilities that power FanCaster's content generation workflow.

Using local inference, FanCaster generates:

- X posts
- Instagram captions
- Match reports
- Headlines
- Blog articles
- Video scripts
- Match summaries

Running AI locally enhances privacy while reducing reliance on external cloud AI services.

---

# Publication Workflow

1. Sports events are received from TxLINE.
2. Events are normalized.
3. Editorial Intelligence evaluates story significance.
4. QVAC generates publication-ready content.
5. Creators review the generated output.
6. Content is published across digital platforms.

---

# Features

- Real-time sports intelligence
- Trusted normalized sports data
- Editorial opportunity detection
- AI-assisted content generation
- Multi-platform publishing workflow
- Modular architecture
- Local AI processing
- Extensible design

---

# Technology Stack

- TxLINE Sports Data API
- QVAC Local AI
- Python
- REST APIs
- Docker
- Modular Service Architecture

---

# Repository Structure

```
FanCaster/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.txt
├── .gitignore
│
├── assets/
│   └── architecture.png
│
├── config/
│   └── settings.py
│
├── docs/
│   ├── Architecture.md
│   └── demo-video.md
│
├── examples/
│   ├── sample_event.json
│   └── generated_post.txt
│
├── src/
│   ├── app/
│   ├── editorial/
│   ├── event_engine/
│   ├── publishing/
│   ├── qvac/
│   └── txline/
│
└── tests/
    └── test_placeholder.py

```

---

# Use Cases

FanCaster is designed for:

- Sports YouTubers
- Sports journalists
- Independent creators
- Digital publishers
- Sports media organizations
- Fan communities

---

# Roadmap

Future enhancements include:

- Support for additional sports
- Multilingual content generation
- AI-powered scheduling
- Team collaboration
- Creator analytics
- Mobile applications
- Plugin ecosystem

---

# Built for the TxODDS Hackathon

FanCaster demonstrates how trusted sports data and local AI can work together to help creators publish faster while maintaining editorial quality.

---

# Contributing

Contributions are welcome.

Please read **CONTRIBUTING.md** before submitting pull requests.

---

# License

This project is licensed under the Apache 2.0 License.

See the LICENSE file for details.

---

## FanCaster

**One Trusted Data Layer. Every Sporting Moment. Infinite Stories.**

