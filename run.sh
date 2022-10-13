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


python -m src.cli --epochs 10 --class-type mlp --name mlp_base --learning-rate 0.001
python -m src.cli --epochs 5 --class-type mlp --name mlp5 --learning-rate 0.001
python -m src.cli --epochs 20 --class-type mlp --name mlp20 --learning-rate 0.001
python -m src.cli --epochs 100 --class-type mlp --name mlp100 --learning-rate 0.001

python -m src.cli --epochs 10 --class-type example --name example_base --learning-rate 0.001
python -m src.cli --epochs 5 --class-type example --name example5 --learning-rate 0.001
python -m src.cli --epochs 20 --class-type example --name example20 --learning-rate 0.001
python -m src.cli --epochs 100 --class-type example --name example100 --learning-rate 0.001