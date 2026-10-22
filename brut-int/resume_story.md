# COMPANY 1 — EY, Data Scientist I, AIQRM (Agent Operations & Evaluation), Sept 2025–Present

## Bullet 1.1
> "Deployed Langfuse observability across 10+ LLM agents, unifying tracing for prompts, tool calls, tokens, and costs; cut agent-debugging time by 35% and enabled real-time monitoring."



--> to is point me mujhe ye btana hai ki mene langfuse tool integrate ya instrumented has bs mene khud ka backend nahi banya hai.

--> to fir vo puchenge thik hai, but how acutally u used langfuse observability


--> to fir mai org me use hue 2 agents (cass aur sustaainbility report scorer) ka example deke ye btaunga ki kese mene langfuse observbiliy ke help se chizo ko consistent labelling k help se obserbe kiya aur kese mene un consistent labelling ko use kr k kis phase/trace me issue hai vo debug kr ek agent-debugging time ko reduce/cut kiya:

    --> Point 1: Designing a consistent instrumentation pattern across the two agents
        
        --> Point 2: Turning raw traces into an actual debugging workflow:
            --> Dono agents ki internal architecture different thi—ek RAG classifier, doosra multi-metric auditor. Maine shared taxonomy define ki: agent, stage, metric_category, aur common stages jaise retrieval, reasoning, scoring, decision, aggregation, jisse cross-agent latency, cost aur failures compare kar sake.

    --> Point 2: Turning raw traces into an actual debugging workflow:
            --> Raw traces se debugging automatically fast nahi hoti. Maine har agent ke failure signals identify karke targeted Langfuse views/alerts banaye—CASS mein retrieval-vs-rule mismatch aur auditor mein metric score variance—taaki engineer directly bug isolate kare, poora trace manually na padhe.