papers = [
    {"title": "Attention Is All You Need", "year": 2017, "citations": 90000, "domain": "NLP"},
    {"title": "BERT: Pre-training of Deep Bidirectional Transformers", "year": 2018, "citations": 70000, "domain": "NLP"},
    {"title": "ImageNet Classification with Deep CNNs", "year": 2012, "citations": 120000, "domain": "Vision"},
    {"title": "Generative Adversarial Nets", "year": 2014, "citations": 55000, "domain": "Generative"},
    {"title": "Deep Residual Learning for Image Recognition", "year": 2016, "citations": 150000, "domain": "Vision"},
    {"title": "GPT-3: Language Models are Few-Shot Learners", "year": 2020, "citations": 40000, "domain": "NLP"},
    {"title": "Adam: A Method for Stochastic Optimization", "year": 2015, "citations": 130000, "domain": "Theory"},
    {"title": "Dropout: Preventing Overfitting", "year": 2014, "citations": 35000, "domain": "Theory"},
]

# 1. Find the paper with the most citations
most_cited = max(papers, key=lambda p: p["citations"])
print("Most cited paper:")
print(f"  {most_cited['title']} — {most_cited['citations']:,} citations")

# 2. Calculate average citations across all papers
avg_citations = sum(p["citations"] for p in papers) / len(papers)
print(f"\nAverage citations: {avg_citations:.2f}")

# 3. Count papers per domain, sorted alphabetically
domain_counts = {}
for p in papers:
    domain = p["domain"]
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

print("\nPapers per domain:")
for domain in sorted(domain_counts):
    print(f"  {domain}: {domain_counts[domain]}")