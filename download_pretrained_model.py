from hf_olmo import OLMoForCausalLM, OLMoTokenizerFast

OLMoForCausalLM.from_pretrained("allenai/OLMo-1B")
OLMoTokenizerFast.from_pretrained("allenai/OLMo-1B")