Let's create a comprehensive set of examples that demonstrate our routing system in action. 

NOTE: In "system_prompt" we are referencing templates by number to keep the examples file clean and it is much more efficient and organized.



### Example1: 

```json
{
  "example": "Example 1",
  "query": "Why does photosynthesis occur?",
  "routing": {
    "thinking": true,
    "web": false,
    "system_prompt": "Template 2: Thinking + No-Web"
  },
  "assistant_response": "# Why Photosynthesis Occurs\n\n## The Fundamental Purpose\n\nPhotosynthesis occurs primarily to convert light energy into chemical energy that organisms can use. This process is essential for life on Earth for several key reasons:\n\n## Energy Conversion\n\n1. **Light to Chemical Energy**: Plants capture sunlight and convert it into glucose (sugar), which serves as stored energy\n2. **ATP Production**: The process generates ATP (adenosine triphosphate), the energy currency of cells\n3. **Carbon Fixation**: It converts inorganic carbon dioxide (CO₂) into organic compounds\n\n## Biological Imperatives\n\n1. **Growth and Development**: The energy produced fuels plant growth, reproduction, and maintenance\n2. **Survival Adaptation**: Photosynthesis evolved as an efficient way to harness abundant solar energy\n3. **Competitive Advantage**: Organisms that could photosynthesize gained access to a virtually unlimited energy source\n\n## Ecological Significance\n\n1. **Oxygen Production**: Photosynthesis releases oxygen as a byproduct, enabling aerobic life\n2. **Food Chain Foundation**: Photosynthetic organisms form the base of most ecosystems\n3. **Carbon Cycle Regulation**: It removes CO₂ from the atmosphere, helping regulate Earth's climate\n\n## The Chemical Logic\n\nAt the molecular level, photosynthesis occurs because:\n- Chlorophyll molecules are uniquely suited to absorb light energy\n- The resulting excited electrons can drive chemical reactions\n- CO₂ and water are readily available raw materials\n- The resulting glucose is a stable, energy-rich compound\n\n## Evolutionary Perspective\n\nPhotosynthesis likely evolved because early Earth had abundant sunlight, water, and CO₂ but limited organic energy sources. Organisms that developed this capability gained a significant survival advantage, leading to the proliferation of photosynthetic life.\n\nThe process continues today because it remains the most efficient way to convert solar energy into biologically useful forms on a global scale."
}
```

### Example2:

```json
{
  "example": "Example 2",
  "query": "What is the last version of python?",
  "routing": {
    "thinking": false,
    "web": true,
    "system_prompt": "Template 3: Non-Thinking + Web"
  },
  "assistant_response": "I don't have access to real-time information to tell you the absolute latest Python version. Python releases new versions regularly, so the most current version changes over time.\n but as of my last update, the latest stable version of Python was Python 3.12. For the current latest version, I recommend checking the official Python website: python.org."
}
```






### Example3:

```json
{
  "example": "Example 3",
  "query": "What are the latest developments in quantum computing?",
  "routing": {
    "thinking": true,
    "web": true,
    "system_prompt": "Template 1: Thinking + Web"
  },
  "assistant_response": "Recent Developments in Quantum Computing\n\n## Hardware Advances\n\n**Increased Qubit Counts:**\n- IBM has expanded its quantum roadmap, with plans for a 1,000+ qubit processor\n- Google and Rigetti continue to improve their superconducting qubit systems\n- IonQ and Honeywell have demonstrated trapped ion systems with improved connectivity\n\n**Error Reduction:**\n- Major breakthroughs in quantum error correction codes\n- Development of more stable qubits with longer coherence times\n- Implementation of error mitigation techniques that improve results without full error correction\n\n## Software and Algorithms\n\n**Quantum Advantage Demonstrations:**\n- Google's quantum supremacy experiment continues to be refined\n- New quantum algorithms for specific optimization problems\n- Hybrid classical-quantum approaches showing promise for near-term applications\n\n**Development Tools:**\n- Expansion of quantum programming frameworks (Qiskit, Cirq, etc.)\n- Cloud-based quantum computing platforms becoming more accessible\n- Improved quantum circuit optimization techniques\n\n## Commercial Applications\n\n**Finance:**\n- Quantum algorithms for portfolio optimization\n- Risk analysis and Monte Carlo simulations\n- Cryptocurrency security analysis\n\n**Pharmaceuticals:**\n- Molecular simulation for drug discovery\n- Protein folding applications\n- Optimization of clinical trials\n\n**Materials Science:**\n- Discovery of new materials with specific properties\n- Optimization of battery technologies\n- Development of more efficient catalysts\n\n## Challenges and Limitations\n\n- Quantum decoherence remains a fundamental challenge\n- Scaling systems while maintaining low error rates\n- High cost and specialized infrastructure requirements\n- Limited availability of quantum talent\n- Need for more robust quantum algorithms for practical applications\n\nThe field continues to evolve rapidly, with both incremental improvements and occasional breakthroughs. While universal quantum computing capable of replacing classical computers is still years away, specialized quantum applications are becoming increasingly viable."
}
```


### Example4:

```json
{
  "example": "Example 4",
  "query": "How do I solve this math equation: 3x + 5 = 14?",
  "routing": {
    "thinking": false,
    "web": false,
    "system_prompt": "Template 4: Non-Thinking + No-Web"
  },
  "assistant_response": "To solve the equation 3x + 5 = 14:\n\nStep 1: Subtract 5 from both sides\n3x + 5 - 5 = 14 - 5\n3x = 9\n\nStep 2: Divide both sides by 3\n3x ÷ 3 = 9 ÷ 3\nx = 3\n\nThe solution is x = 3.\n\nYou can verify this by substituting 3 back into the original equation:\n3(3) + 5 = 9 + 5 = 14 ✓"
}
```

### Example5:
```json
{
  "example": "Example 5",
  "query": "How should I invest $10,000 in today's market?",
  "routing": {
    "thinking": true,
    "web": true,
    "system_prompt": "Template 1: Thinking + Web"
  },
  "assistant_response": "# Investment Considerations for $10,000\n\n## Important Disclaimer\n\nI am not a financial advisor, and this information should not be considered personalized financial advice. Investment decisions should be made based on your personal financial situation, risk tolerance, and goals. Consider consulting with a qualified financial professional before making investment decisions.\n\n## Factors to Consider\n\n**Your Financial Situation:**\n- Do you have an emergency fund (3-6 months of expenses)?\n- Are you carrying high-interest debt (credit cards, etc.)?\n- What is your time horizon for this investment?\n- What is your risk tolerance?\n\n**Current Market Conditions:**\n- Interest rates have been rising, affecting both bonds and stocks\n- Inflation concerns remain elevated\n- Geopolitical tensions are creating market volatility\n- Technology sector has seen significant fluctuations\n\n## Investment Approaches\n\n**Conservative Approach (Lower Risk):**\n- High-yield savings accounts (currently offering competitive rates)\n- Short-term Treasury bills or CDs\n- Money market funds\n- I Bonds (inflation-protected government bonds)\n\n**Moderate Approach (Balanced Risk):**\n- Diversified index funds (S&P 500, total market)\n- Target-date funds based on your time horizon\n- Balanced mutual funds (mix of stocks and bonds)\n- Real estate investment trusts (REITs)\n\n**Aggressive Approach (Higher Risk):**\n- Individual stocks in sectors you understand\n- Sector-specific ETFs (technology, healthcare, etc.)\n- Emerging market funds\n- Cryptocurrency (only a small portion of your portfolio)\n\n## Diversification Strategy\n\nRegardless of your approach, consider:\n- Spreading investments across different asset classes\n- Avoiding concentration in a single stock or sector\n- Regular rebalancing to maintain your target allocation\n- Dollar-cost averaging rather than timing the market\n\n## Next Steps\n\n1. Assess your personal financial situation and goals\n2. Determine your risk tolerance\n3. Research specific investment options\n4. Consider opening an investment account (brokerage, IRA, etc.)\n5. Start with a small portion while you learn\n6. Review and adjust your strategy periodically\n\nThe best investment strategy depends on your individual circumstances, time horizon, and comfort with risk."
}
```

### Example6:
```json
{
  "example": "Example 6",
  "query": "What are the top-rated restaurants in New York City right now?",
  "routing": {
    "thinking": false,
    "web": false,
    "system_prompt": "Template 3: Non-Thinking + Web"
  },
  "assistant_response": "I don't have access to current restaurant ratings and reviews as they change frequently. For the most up-to-date information on top-rated restaurants in New York City, I recommend checking:\n\n- Michelin Guide (for starred restaurants)\n- The New York Times restaurant reviews\n- Zagat guide\n- OpenTable or Resy (for current availability and reviews)\n- Yelp or Google Reviews (for customer ratings)\n\nThese sources provide regularly updated ratings and reviews based on professional critics and diner feedback. Restaurant rankings can change frequently due to new openings, chef changes, or updated reviews, so checking these current sources will give you the most accurate information.\n\nWould you like me to provide information about any specific type of cuisine or dining experience in NYC that I can help with based on my general knowledge?"
}
```


### Example7:
```json
{
  "example": "Example 7",
  "query": "What is type 2 diabetes and how does it develop?",
  "routing": {
    "thinking": true,
    "web": false,
    "system_prompt": "Template 2: Thinking + No-Web"
  },
  "assistant_response": "# Type 2 Diabetes: Understanding the Condition\n\n## What is Type 2 Diabetes?\n\nType 2 diabetes is a chronic metabolic disorder characterized by high blood sugar levels (hyperglycemia) resulting from the body's ineffective use of insulin or relative insulin deficiency. It's the most common form of diabetes, accounting for about 90-95% of all diabetes cases.\n\n## How Type 2 Diabetes Develops\n\n### Insulin Resistance\n\n1. **Normal Function**: In a healthy body, insulin (produced by the pancreas) helps cells absorb glucose from the bloodstream for energy.\n\n2. **Resistance Development**: In type 2 diabetes, cells become resistant to insulin's effects, meaning they don't respond efficiently to insulin signals.\n\n3. **Pancreatic Compensation**: Initially, the pancreas compensates by producing more insulin to overcome this resistance.\n\n4. **Pancreatic Fatigue**: Over time, the pancreas may become unable to produce enough insulin to maintain normal blood sugar levels.\n\n### Progressive Nature\n\nType 2 diabetes typically develops gradually over years, often progressing through these stages:\n\n1. **Insulin Resistance**: Cells become less responsive to insulin\n2. **Prediabetes**: Blood sugar levels are higher than normal but not yet diabetic\n3. **Type 2 Diabetes**: Blood sugar levels consistently exceed diabetic thresholds\n\n## Risk Factors\n\n**Modifiable Risk Factors:**\n- Excess body weight, particularly abdominal obesity\n- Physical inactivity\n- Unhealthy diet high in processed foods and sugar\n- Smoking\n- Excessive alcohol consumption\n\n**Non-Modifiable Risk Factors:**\n- Age (risk increases after 45)\n- Family history and genetics\n- Ethnicity (higher risk in certain populations)\n- History of gestational diabetes\n\n## Pathophysiology\n\nThe development of type 2 diabetes involves multiple mechanisms:\n\n1. **Genetic Predisposition**: Multiple genes contribute to susceptibility\n2. **Lifestyle Factors**: Diet and exercise significantly impact risk\n3. **Metabolic Dysfunction**: Abnormal fat metabolism contributes to insulin resistance\n4. This information is for educational purposes only and should not be considered medical advice. If you have concerns about diabetes or your health:\n\n- Consult with a healthcare professional for personalized medical advice\n- Get regular check-ups and blood sugar screenings if you have risk factors\n- Follow your doctor's recommendations for prevention and treatment\n- Seek immediate medical attention for severe symptoms like extreme thirst, frequent urination, unexplained weight loss, or blurred vision\n\nType 2 diabetes is a serious medical condition that requires professional medical management, including lifestyle modifications and possibly medication."
}
```


### Example8:
```json
{
  "example": "Example 8",
  "query": "What time is it in Tokyo right now?",
  "routing": {
    "thinking": false,
    "web": true,
    "system_prompt": "Template 3: Non-Thinking + Web"
  },
  "assistant_response": "I don't have access to real-time clock information. To find the current time in Tokyo, Japan, I recommend:\n\n- Searching \"current time in Tokyo\" in your search engine\n- Using a world clock website or app\n- Checking your smartphone's world clock feature\n\nTokyo is in the Japan Standard Time (JST) zone, which is UTC+9. This means Tokyo is:\n- 9 hours ahead of UTC\n- 14 hours ahead of Eastern Time (ET)\n- 17 hours ahead of Pacific Time (PT)\n\nNote that Japan does not observe daylight saving time, so the time difference remains constant throughout the year."
}
```


### Example9:
```json
{
  "example": "Example 9",
  "query": "Can I break my work contract before it ends without penalties?",
  "routing": {
    "thinking": false,
    "web": false,
    "system_prompt": "Template 4: Non-Thinking + No-Web"
  },
  "assistant_response": "I cannot provide specific legal advice about breaking your work contract, as employment law varies significantly by jurisdiction and depends on the specific terms of your contract. This is a matter that requires professional legal guidance.\n\n**Why you need legal advice:**\n- Employment laws differ by state/province and country\n- Your contract terms are legally binding and may include specific clauses\n- Consequences for breaking contracts can include financial penalties or legal action\n- There may be exceptions or protections that apply to your situation\n- Recent legal changes might affect your rights and obligations\n\n**An employment law attorney can help you understand:**\n- The specific terms and enforceability of your contract\n- Any notice periods or penalty clauses that apply\n- Potential defenses or exceptions that might be available\n- The legal process for terminating your employment\n- Your rights regarding final pay, benefits, and references\n- Whether negotiation with your employer is possible\n\n**General factors that may be relevant (not legal advice):**\n- The type of employment contract you have\n- Whether you're in an \"at-will\" employment jurisdiction\n- Any specific termination clauses in your agreement\n- The reason for wanting to terminate the contract\n- Your position and level within the organization\n- Whether there have been any breaches by your employer\n\n**Next steps:**\n- Review your employment contract carefully\n- Document any relevant circumstances or issues\n- Consult with an employment law attorney before taking action\n- Consider whether negotiation with your employer might be appropriate\n\n**Finding legal help:**\n- Contact your local bar association for employment law attorney referrals\n- Look for attorneys who offer free initial consultations\n- Check if your employer provides access to legal assistance programs\n- Consider legal aid services if you have limited financial resources\n\nEmployment contract issues can have serious financial and career implications, so professional legal guidance is essential before making any decisions."
}
```


### Example10:
```json
{
  "example": "Example 10",
  "query": "Why does overfitting happen in neural networks?",
  "routing": {
    "thinking": true,
    "web": false,
    "system_prompt": "Template 2: Thinking + No-Web"
  },
  "assistant_response": "Overfitting happens when a model learns patterns that are specific to the training data rather than patterns that generalize well to new, unseen data. This usually occurs when the model is too complex compared to the amount or quality of training data, causing it to memorize noise instead of learning the underlying signal.\n\nAs a result, an overfitted model performs very well on the training set but poorly on validation or test data. Common signs of overfitting include a large gap between training performance and test performance.\n\nOverfitting can be reduced using techniques such as simplifying the model, collecting more training data, applying regularization, using dropout (for neural networks), or stopping training early based on validation performance. The goal is to balance model complexity so it captures meaningful patterns without fitting noise."
}
```