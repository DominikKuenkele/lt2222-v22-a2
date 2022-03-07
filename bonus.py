import mycode as mc

sampled_lines = mc.sample_lines("data/UN-english.txt.gz", lines=100000)
processed_sentences = mc.process_sentences(sampled_lines)
all_samples = mc.create_samples(processed_sentences, samples=50000)
fulldf = mc.create_df(all_samples)
train_X, train_y, test_X, test_y = mc.split_samples(fulldf, test_percent=20)
model_mlp = mc.train_mlp(train_X, train_y)

mc.eval_model(model_mlp, test_X, test_y)
