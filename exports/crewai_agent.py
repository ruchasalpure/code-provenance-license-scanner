from crewai import Agent

code_provenance_license_scanner = Agent(
    role="Code Provenance License Scanner",
    goal="Deliver high-precision autonomous Code Provenance License Scanner operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
