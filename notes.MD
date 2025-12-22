ai-investment-agent/
│
├── README.md
├── .gitignore
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── entrypoint.sh
│
├── app/                      # Application layer
│   ├── main.py               # Streamlit entry
│   ├── config/
│   │   ├── settings.py
│   │   └── logging.py
│   │
│   ├── ui/
│   │   ├── intake_page.py
│   │   └── components.py
│   │
│   ├── agents/
│   │   ├── intake_agent.py
│   │   ├── market_scanner.py      # Phase 2
│   │   ├── research_agent.py      # Phase 2
│   │   └── decision_agent.py      # Phase 3
│   │
│   ├── services/
│   │   ├── market_data.py
│   │   ├── etf_service.py
│   │   ├── sector_service.py
│   │   └── robinhood_links.py
│   │
│   ├── llm/
│   │   ├── client.py
│   │   ├── prompts/
│   │   │   ├── intake.txt
│   │   │   ├── strategy.txt
│   │   │   └── summary.txt
│   │   └── response_parser.py
│   │
│   ├── models/
│   │   ├── preferences.py
│   │   ├── stock.py
│   │   └── etf.py
│   │
│   ├── storage/
│   │   ├── local_store.py
│   │   └── sqlite.db
│   │
│   └── utils/
│       ├── validators.py
│       ├── constants.py
│       └── helpers.py
│
├── data/
│   ├── sectors.yaml
│   ├── etfs.yaml
│   └── universe.yaml
│
├── tests/
│   ├── test_intake_agent.py
│   ├── test_market_data.py
│   └── test_etf_cagr.py
│
├── scripts/
│   ├── preload_etfs.py
│   └── sanity_check.py
│
├── requirements.txt
├── pyproject.toml
└── Makefile
