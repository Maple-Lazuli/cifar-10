python -m src.cli --epochs 10 --class-type lenet --name lenet_base --learning-rate 0.001
python -m src.cli --epochs 5 --class-type lenet --name lenet5 --learning-rate 0.001
python -m src.cli --epochs 20 --class-type lenet --name lenet20 --learning-rate 0.001
python -m src.cli --epochs 100 --class-type lenet --name lenet100 --learning-rate 0.001

python -m src.cli --epochs 10 --class-type lenet --name lenet_small_batch --learning-rate 0.001 --batch_size 60
python -m src.cli --epochs 10 --class-type lenet --name lenet_large_batch --learning-rate 0.001 --batch_size 800
python -m src.cli --epochs 10 --class-type lenet --name lenet_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type lenet --name lenet_small_lr --learning-rate 0.0001
python -m src.cli --epochs 10 --class-type lenet --name lenet_large_lr --learning-rate 0.01