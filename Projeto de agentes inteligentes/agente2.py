from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from agente import llm, ferramentas, HumanMessage, SYSTEM_PROMPT

memory = MemorySaver()

agent = create_agent(model= llm, tools=ferramentas, system_prompt=SYSTEM_PROMPT) #checkpointer=memory)

config = {"configurable": {"thread_id": "sessao1"}}
if __name__ == "__main__":
    prompts = [
        "meu nome é Stella", 
        "como funciona o program de fidelidade?", 
        "quantos pontos eu tenho?"
    ]
    for prompt in prompts: 
        print(agent.invoke(
            {"messages":
                [HumanMessage(content=prompt)]
                }, config=config)["messages"][-1].content)