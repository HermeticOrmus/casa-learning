# Card Template

Transform raw captures into structured, reviewable knowledge cards.

---

### Card [N] - [Term Name]

**Q**: [Question that tests understanding - not just recall]

**A**: [Concise answer - 1-2 sentences max]

**ELI5:**
[Your personal analogy. Reference your interests, not generic examples.]

**Commands/Code:**
```bash
# What to type in terminal / editor
# Make it copy-paste ready
command --flags arguments
```

**Use Cases:**
- [Real scenario 1 where you'd use this]
- [Real scenario 2 - ideally from your projects]
- [Real scenario 3 - or career context]

**Connections:**
- Related to: [[Other Card]]
- Builds on: [[Prerequisite Concept]]
- Leads to: [[Advanced Topic]]

**Tags**: #domain #type #difficulty

**Source**: [Course/Book/Video] - [Section/Chapter]

---

## Card Quality Checklist

- [ ] Question tests *understanding*, not just recall
- [ ] Answer is concise (can you explain in 10 seconds?)
- [ ] ELI5 uses YOUR personal reference
- [ ] Code is copy-paste ready and tested
- [ ] Use cases are specific, not vague
- [ ] Tags will help future retrieval
- [ ] Source is traceable

## Question Types That Work

| Type | Example | Why It Works |
|------|---------|--------------|
| **How** | "How does X achieve Y?" | Tests mechanism understanding |
| **When** | "When would you use X over Y?" | Tests contextual judgment |
| **Why** | "Why does X require Y?" | Tests causal understanding |
| **What if** | "What happens if X fails?" | Tests edge case knowledge |

## Question Types to Avoid

| Type | Example | Why It Fails |
|------|---------|--------------|
| **Define** | "What is X?" | Encourages rote memorization |
| **List** | "What are the 5 types of X?" | Tests memory, not understanding |
| **True/False** | "X is faster than Y. T/F?" | 50% guess rate |

---

## Example Card

### Card 12 - TCP Three-Way Handshake

**Q**: Why does TCP require three messages to establish a connection instead of two?

**A**: Both sides need to confirm they can send AND receive. Two messages only confirms one direction.

**ELI5:**
It's like the start of a Dragon Ball Z fight. Goku powers up (SYN), Vegeta responds with his power-up (SYN-ACK), then Goku acknowledges "I see your power level" (ACK). Now both know the other is ready. If Goku just attacked without waiting for Vegeta's response, he wouldn't know if Vegeta was even paying attention.

**Commands/Code:**
```bash
# Watch a three-way handshake in real-time
sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0' -nn

# Filter in Wireshark
tcp.flags.syn == 1 || tcp.flags.ack == 1
```

**Use Cases:**
- Debugging connection timeouts (which step is failing?)
- Understanding SYN flood attacks (why they exhaust resources)
- Firewall rules (stateful vs stateless inspection)

**Connections:**
- Related to: [[TCP vs UDP]]
- Builds on: [[Network Layers]]
- Leads to: [[Connection States]]

**Tags**: #networking #tcp #protocol #fundamentals

**Source**: TryHackMe - Networking Fundamentals - Task 4
