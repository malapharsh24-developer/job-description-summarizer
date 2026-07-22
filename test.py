import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

def main():
    print("================ JOB Description Summarizer! =====================")
    
    # dotenv config
    load_dotenv()
    
    # API KEY
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
    
    # text data
    information = """
    Job Title: React.js Developer

Company: TechNova Solutions Pvt. Ltd.

Location: Pune, Maharashtra (Hybrid)

Experience: 2–4 Years

Job Type: Full-Time

Job Description:

TechNova Solutions is looking for a passionate React.js Developer to join our Product Engineering team. The ideal candidate should have experience building responsive web applications using React.js and integrating frontend applications with RESTful APIs.

Key Responsibilities:
- Develop, maintain, and optimize React.js applications.
- Build reusable UI components and ensure responsive design.
- Integrate frontend applications with REST APIs developed in .NET Core.
- Collaborate with UI/UX designers to convert Figma designs into pixel-perfect interfaces.
- Write clean, maintainable, and well-documented code.
- Debug, test, and resolve application issues.
- Participate in code reviews and Agile Scrum ceremonies.
- Work closely with backend developers and QA teams.

Required Skills:
- Strong knowledge of React.js, JavaScript (ES6+), HTML5, and CSS3.
- Experience with Redux or Context API.
- Familiarity with REST APIs and JSON.
- Good understanding of Git and GitHub.
- Basic knowledge of SQL and writing simple queries.
- Experience with responsive web development.

Preferred Skills:
- Knowledge of .NET Core or ASP.NET MVC.
- Experience with Tailwind CSS or Bootstrap.
- Familiarity with Azure DevOps or Jira.
- Understanding of CI/CD pipelines.

Qualifications:
- Bachelor's degree in Computer Science, Information Technology, or a related field.
- 2–4 years of professional experience in frontend development.

Benefits:
- Hybrid work model.
- Health insurance.
- Performance bonus.
- Learning and certification reimbursement.
- Flexible working hours.
    """
    
    
    # prompt template for summary
    summary_template = """
    Summarize the following Job Description in 60-100 words.

    Focus on:
    - Role and purpose
    - Key responsibilities
    - Required skills and technologies
    - Experience required
    - Location (if available)

    Keep the summary concise, professional, and based only on the provided information.

    Job Description:
    {information}

    Summary:
    """
    
    # langchain prompt template set up
    summary_prompt_template = PromptTemplate(input_variables=["information"], template = summary_template)
    
    

    # chat model
    llm = init_chat_model("google_genai:gemini-3.5-flash-lite",api_key = GOOGLE_API_KEY, temperature=0)
    
    chain = summary_prompt_template | llm
    
    response = chain.invoke(input={"information":information})
    
    print(20*"=","\n\n")
    print(response.text,"\n\n",20*"=")
    


if __name__ == "__main__":
    main()
