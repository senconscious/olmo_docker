from hf_olmo import OLMoForCausalLM, OLMoTokenizerFast

olmo = OLMoForCausalLM.from_pretrained("allenai/OLMo-1B")
tokenizer = OLMoTokenizerFast.from_pretrained("allenai/OLMo-1B")
message = ["Language modeling is "]
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
# optional verifying cuda
# inputs = {k: v.to('cuda') for k,v in inputs.items()}
# olmo = olmo.to('cuda')
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])