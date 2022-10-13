python -m src.cli --epochs 10 --class-type mlp --name mlp_small_batch --learning-rate 0.001 --batch_size 60
python -m src.cli --epochs 10 --class-type mlp --name mlp_large_batch --learning-rate 0.001 --batch_size 800
python -m src.cli --epochs 10 --class-type mlp --name mlp_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type mlp --name mlp_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type mlp --name mlp_large_lr --learning-rate 0.01

python -m src.cli --epochs 10 --class-type example --name example_small_batch --learning-rate 0.001 --batch_size 60
python -m src.cli --epochs 10 --class-type example --name example_large_batch --learning-rate 0.001 --batch_size 800
python -m src.cli --epochs 10 --class-type example --name example_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type example --name example_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type example --name example_large_lr --learning-rate 0.01